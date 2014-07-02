from django.shortcuts import render, get_object_or_404
from website.models import NewsArticle, AlertCampaign, NewsLetter, EducationalArticle, BannerCampaign, HomePageCampaign
from website.models import GalleryArticle, SpecialArticle
from django.db.models import Q
from django.utils.safestring import mark_safe
from django.utils.html import escape
from datetime import datetime


# Create your views here.
def gallery_index(request):
    article_list = GalleryArticle.objects.all().order_by('-pub_date')[:10]
    context = {
        'article_list': article_list,
        'url_namespace': 'gallery:article',
        'read_on_message': 'View the pictures...'
    }
    update_context(request, context)
    return render(request, 'website/gallery/index.html', context)


def gallery_article(request, article_id):
    article = get_object_or_404(GalleryArticle, slug=article_id)
    context = {'article': article}
    update_context(request, context)
    return render(request, 'website/gallery/article.html', context)


def home_index(request):
    banner_campaigns = BannerCampaign.objects.all().filter(
        Q(expiry__gte=datetime.today()) |
        Q(expiry__isnull=True)
    )
    home_page_campaigns = HomePageCampaign.objects.all().filter(
        Q(expiry__gte=datetime.today()) |
        Q(expiry__isnull=True)
    )[:4]
    context = {
        'banner_campaigns': banner_campaigns,
        'home_page_campaigns': home_page_campaigns
    }
    update_context(request, context)
    return render(request, 'website/home/index.html', context)


def news_index(request):
    article_list = NewsArticle.objects.all().order_by('-pub_date')[:10]
    context = {
        'article_list': article_list,
        'url_namespace': 'news:article',
        'read_on_message': 'Read on for more details...'
    }
    update_context(request, context)
    return render(request, 'website/news/index.html', context)


def news_index_by_year(request, year):
    article_list = NewsArticle.objects.all().order_by('-pub_date')
    article_list = article_list.filter(pub_date__year=year)
    context = {
        'article_list': article_list,
        'url_namespace': 'news:article',
        'read_on_message': 'Read on for more details...'
    }
    update_context(request, context)
    return render(request, 'website/news/index.html', context)


def news_article(request, article_id):
    response = get_object_or_404(NewsArticle, slug=article_id)
    (request, context) = article_parse(request, response)
    return render(request, 'website/news/article.html', context)


def news_newsletter(request):
    newsletter_list = NewsLetter.objects.all().order_by('-pub_date')
    context = {'newsletter_list': newsletter_list}
    update_context(request, context)
    return render(request, 'website/news/newsletter.html', context)


def rss_index(request):
    article_list = NewsArticle.objects.all().order_by('-pub_date')
    context = {
        'article_list': article_list
    }
    return render(request, 'website/rss/index.xml', context)


def rss_limit(request, count):
    article_list = NewsArticle.objects.all().order_by('-pub_date')[:count]
    context = {
        'article_list': article_list
    }
    return render(request, 'website/rss/index.xml', context)


def education_index(request):
    article_list = EducationalArticle.objects.all().order_by('-pub_date')[:10]
    context = {
        'article_list': article_list,
        'url_namespace': 'education:article',
        'read_on_message': 'Read on for more details...'
    }
    update_context(request, context)
    return render(request, 'website/education/index.html', context)


def education_article(request, article_id):
    response = get_object_or_404(EducationalArticle, slug=article_id)
    (request, context) = article_parse(request, response)
    return render(request, 'website/education/article.html', context)


def news_newsletter_by_issue(request, issue):
    newsletter_list = NewsLetter.objects.all()
    newsletter_list = newsletter_list.filter(issue_number=issue)
    context = {'newsletter_list': newsletter_list}
    update_context(request, context)
    return render(request, 'website/news/newsletter.html', context)


def news_newsletter_by_year(request, year):
    newsletter_list = NewsLetter.objects.all()
    newsletter_list = newsletter_list.filter(pub_date__year=year)
    context = {'newsletter_list': newsletter_list}
    update_context(request, context)
    return render(request, 'website/news/newsletter.html', context)


def news_newsletter_by_month(request, year, month):
    newsletter_list = NewsLetter.objects.all()
    newsletter_list = newsletter_list.filter(pub_date__year=year)
    # MongoDB does not support month/day queries
    newsletter_list = newsletter_list.filter(pub_date__month=month)
    context = {'newsletter_list': newsletter_list}
    update_context(request, context)
    return render(request, 'website/news/newsletter.html', context)


def special_article(request, article_id):
    response = get_object_or_404(SpecialArticle, slug=article_id)
    (request, context) = article_parse(request, response)
    if response.template == SpecialArticle.STANDARD:
        return render(request, 'website/special/article.html', context)
    if response.template == SpecialArticle.MULTI_IMAGE:
        return render(request, 'website/special/multi-image.html', context)


def contact_form(request):
    response = get_object_or_404(SpecialArticle, slug='contact')
    context = {'article': response}
    update_context(request, context)
    return render(request, 'website/special/contact.html', context)


# helpers
def article_parse(request, response):
    split_content = parse_text(response.articlecontent.full)
    response.first_paragraph = split_content[0] if len(split_content) > 0 else ''
    if len(split_content) > 1:
        response.rest_of_paragraphs = split_content[1:]
    context = {'article': response}
    update_context(request, context)
    return request, context


def parse_text(content):
    # separate paragraphs
    split_content = content.split("\r\n\r\n")

    # remove empty paragraphs
    split_content = [x for x in split_content if x]

    # mark autoescape tagged paragraphs
    for x in range(len(split_content)):
        if split_content[x].startswith(':safe:'):
            split_content[x] = split_content[x].replace(':safe:', '')
            split_content[x] = mark_safe(split_content[x])
        else:
            split_content[x] = escape(split_content[x])
    return split_content


def update_context(request, context):
    """adds fields to context for templates"""
    context['alert_campaign'] = alert_campaign(request)
    context['viewed_campaign'] = viewed_campaign(request)
    context['news_years'] = news_years()
    return context


def alert_campaign(request):
    """get current alert campaigns"""
    campaigns = AlertCampaign.objects.filter(
        Q(expiry__gte=datetime.today()) |
        Q(expiry__isnull=True)
    )
    for cookie in request.COOKIES:
        campaigns = campaigns.exclude(slug=cookie)
    return campaigns


def viewed_campaign(request):
    """set cookie for direct visit of alert campaign url"""
    campaigns = AlertCampaign.objects.filter(
        article=request.path
    )
    return campaigns


def news_years():
    """get list of years with news"""
    article_dates = NewsArticle.objects.dates('pub_date','year')
    return sorted([date.year for date in article_dates], reverse=True)
    # return [x for x in range(2014, 2007, -1)]
