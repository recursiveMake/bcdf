__author__ = 'adonis'

from website.models import AlertCampaign, EducationalArticle, NewsArticle
from django.utils.safestring import mark_safe
from django.utils.html import escape
from datetime import datetime
from django.db.models import Q


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
    context['education_years'] = education_years()
    return context


def alert_campaign(request):
    """get current alert campaigns"""
    campaigns = AlertCampaign.objects.filter(
        Q(expiry__gte=datetime.today()) |
        Q(expiry__isnull=True)
    )
    for cookie in request.COOKIES:
        campaigns = campaigns.exclude(slug=cookie)
    if campaigns.count() > 1:
        campaigns = [campaigns[0]]
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


def education_years():
    """get list of years with educational articles"""
    article_dates = EducationalArticle.objects.dates('pub_date','year')
    return sorted([date.year for date in article_dates], reverse=True)
