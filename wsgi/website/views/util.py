__author__ = 'adonis'

from website.models import AlertCampaign, EducationalArticle, NewsArticle, NewsLetter
from django.utils.safestring import mark_safe
from django.utils.html import escape
from datetime import datetime, timedelta
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render as shortcut_render


def paginate(request, obj_list, items_per_page=10):
    paginator = Paginator(obj_list, items_per_page)
    page = request.GET.get('page')
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    return result


def article_parse(request, response):
    split_content = parse_text(response.articlecontent.full)
    response.first_paragraph = split_content[0] if len(split_content) > 0 else ''
    if len(split_content) > 1:
        response.rest_of_paragraphs = split_content[1:]
    context = {'article': response}
    return request, context


def parse_text(content):
    # separate paragraphs
    split_content = content.replace('\r', '').split("\n\n")

    # remove empty paragraphs
    split_content = [x for x in split_content if x]

    # mark autoescape tagged paragraphs
    for x in range(len(split_content)):
        if split_content[x].startswith(':safe:'):
            split_content[x] = split_content[x].replace(':safe:', '')
            split_content[x] = mark_safe(split_content[x])
        # we really need to get MarkDown in here
        elif split_content[x].startswith(':table:'):
            split_content[x] = split_content[x].replace(':table:', '')
            split_content[x] = parse_table(split_content[x])
            split_content[x] = mark_safe(split_content[x])
        else:
            split_content[x] = escape(split_content[x])
    return split_content


def parse_table(content):
    rows = []
    for row in content.split("\r\n"):
        if row:
            rows.append(row.split('|'))

    table = '<table class="table table-striped">'

    # title
    table += '<thead><tr>'
    if len(rows) > 0:
        for cell in rows[0]:
            table += '<th>' + cell + '</th>'
    table += '</tr></thead>'

    # body
    table += '<tbody>'
    if len(rows) > 1:
        for row in rows[1:]:
            table += '<tr>'
            for cell in row:
                table += '<td>' + cell + '</td>'
            table += '</tr>'
    table += '</tbody>'
    table += '</table>'
    return table


def update_context(request, context):
    """adds fields to context for templates"""
    context['alert_campaign'] = alert_campaign(request)
    context['news_years'] = news_years()
    context['newsletter_years'] = newsletter_years()
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
    viewed_campaigns = viewed_campaign(request)
    for campaign in viewed_campaigns:
        campaigns = campaigns.exclude(slug=campaign.slug)
    if campaigns.count() > 1:
        campaigns = [campaigns[0]]
    return campaigns


def viewed_campaign(request):
    """list of viewed campaigns on current page"""
    slug = ''
    if not request.resolver_match:
        return []
    if request.resolver_match.args:
        slug = request.resolver_match.args[0]
    elif request.resolver_match.kwargs:
        key = list(request.resolver_match.kwargs.keys())[0]
        slug = request.resolver_match.kwargs[key]
    campaigns = AlertCampaign.objects.filter(
        article_namespace=request.resolver_match.view_name,
        article_slug=slug
    )
    return campaigns


def update_response(request, response):
    """set cookie for direct visit of alert campaign url"""
    campaigns = viewed_campaign(request)
    for campaign in campaigns:
        response.set_cookie(
            key=campaign.slug,
            value='VIEWED',
            expires=datetime.now() + timedelta(days=campaign.snooze_long)
        )
    return response


def news_years():
    """get list of years with news"""
    article_dates = NewsArticle.objects.dates('pub_date','year')
    return sorted([date.year for date in article_dates], reverse=True)
    # return [x for x in range(2014, 2007, -1)]


def newsletter_years():
    """get list of years with newsletters"""
    newsletter_dates = NewsLetter.objects.dates('pub_date', 'year')
    return sorted([date.year for date in newsletter_dates], reverse=True)


def education_years():
    """get list of years with educational articles"""
    article_dates = EducationalArticle.objects.dates('pub_date','year')
    return sorted([date.year for date in article_dates], reverse=True)


def render(request, template, context, **kwargs):
    update_context(request, context)
    response = shortcut_render(request, template, context, **kwargs)
    return update_response(request, response)