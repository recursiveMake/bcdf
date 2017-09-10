__author__ = 'adonis'


from website.models import CalendarCampaign
from website.models import NewsArticle
from website.views.util import render, paginate
import datetime


def get_article(calendar_item):
    article = None
    try:
        article = NewsArticle.objects.get(slug=calendar_item.article_slug)
    except (NewsArticle.DoesNotExist, NewsArticle.MultipleObjectsReturned):
        pass
    return article


def update_article(article, calendar_item):
    article.title = calendar_item.title
    article.pub_date = calendar_item.expiry
    if calendar_item.blurb:
        article.articlecontent.short = calendar_item.blurb
    return article


def calendar_index(request):
    calendar_list = CalendarCampaign.objects.published(request.production).filter(
        expiry__gte=datetime.date.today()).order_by('expiry')
    article_list = []
    for item in calendar_list:
        article = get_article(item)
        if article:
            article_list.append(update_article(article, item))
    article_list = paginate(request, article_list)
    context = {
        'article_list': article_list,
        'url_namespace': 'news:article',
        'read_on_message': 'Read on for more details...'
    }
    return render(request, 'website/calendar/index.html', context)