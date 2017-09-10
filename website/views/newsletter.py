__author__ = 'adonis'


from website.models import NewsLetter
from website.views.util import render
from django.shortcuts import get_object_or_404


def news_newsletter(request):
    newsletter_list = NewsLetter.objects.published(request.production).order_by('-pub_date')
    context = {'newsletter_list': newsletter_list}
    return render(request, 'website/news/newsletter.html', context)


def news_newsletter_by_issue(request, issue):
    newsletter_list = NewsLetter.objects.published(request.production)
    newsletter_list = newsletter_list.filter(issue_number=int(issue))
    context = {'newsletter_list': newsletter_list}
    return render(request, 'website/news/newsletter.html', context)


def news_newsletter_by_year(request, year):
    newsletter_list = NewsLetter.objects.published(request.production)
    newsletter_list = newsletter_list.filter(pub_date__year=year)
    context = {'newsletter_list': newsletter_list}
    return render(request, 'website/news/newsletter.html', context)


def news_newsletter_by_slug(request, article_id):
    newsletter_list = [get_object_or_404(NewsLetter.objects.published(request.production), slug=article_id)]
    context = {'newsletter_list': newsletter_list}
    return render(request, 'website/news/newsletter.html', context)


def news_newsletter_by_month(request, year, month):
    newsletter_list = NewsLetter.objects.published(request.production)
    newsletter_list = newsletter_list.filter(pub_date__year=year)
    # MongoDB does not support month/day queries
    newsletter_list = newsletter_list.filter(pub_date__month=month)
    context = {'newsletter_list': newsletter_list}
    return render(request, 'website/news/newsletter.html', context)
