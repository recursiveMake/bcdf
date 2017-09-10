__author__ = 'adonis'


from website.models import NewsArticle
from website.views.util import render, article_parse, paginate
from django.shortcuts import get_object_or_404


def news_index(request):
    article_list = NewsArticle.objects.published(request.production).order_by('-pub_date')
    article_list = paginate(request, article_list)
    context = {
        'article_list': article_list,
        'url_namespace': 'news:article',
        'read_on_message': 'Read on for more details...'
    }
    return render(request, 'website/news/index.html', context)


def news_index_by_year(request, year):
    article_list = NewsArticle.objects.published(request.production).order_by('-pub_date')
    article_list = article_list.filter(pub_date__year=year)
    article_list = paginate(request, article_list)
    context = {
        'article_list': article_list,
        'url_namespace': 'news:article',
        'read_on_message': 'Read on for more details...'
    }
    return render(request, 'website/news/index.html', context)


def news_article(request, article_id):
    response = get_object_or_404(NewsArticle.objects.published(request.production), slug=article_id)
    (request, context) = article_parse(request, response)
    return render(request, 'website/news/article.html', context)
