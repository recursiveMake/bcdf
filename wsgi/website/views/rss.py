__author__ = 'adonis'


from website.models import NewsArticle, GalleryArticle, EducationalArticle
from django.shortcuts import render, get_object_or_404


def rss_index(request):
    return rss_limit(request)

def rss_limit(request, count=None):
    news_article_list = NewsArticle.objects.all().order_by('-pub_date')[:count]
    gallery_article_list = GalleryArticle.objects.all().order_by('-pub_date')[:count]
    educational_article_list = EducationalArticle.objects.all().order_by('-pub_date')[:count]
    article_list = sorted(
        news_article_list + gallery_article_list + educational_article_list,
        key=lambda x : x.pub_date,
        reverse=True
    )[:count]
    context = {
        'article_list': article_list
    }
    return render(request, 'website/rss/index.xml', context)

def rss_feed(request, feed):
    return rss_feed_limit(request, feed)

def rss_feed_limit(request, feed, count=None):
    feed = feed.lower()
    if feed == 'photos':
        return photos_xml(request, count)
    elif feed == 'education':
        return education_xml(request, count)
    elif feed == 'news':
        return news_xml(request, count)

def photos_xml(request, count=None):
    article_list = GalleryArticle.objects.all().order_by('-pub_date')[:count]
    context = {
        'article_list': article_list
    }
    return render(request, 'website/rss/photos.xml', context)

def education_xml(request, count=None):
    article_list = EducationalArticle.objects.all().order_by('-pub_date')[:count]
    context = {
        'article_list': article_list
    }
    return render(request, 'website/rss/education.xml', context)

def news_xml(request):
    article_list = NewsArticle.objects.all().order_by('-pub_date')
    context = {
        'article_list': article_list
    }
    return render(request, 'website/rss/news.xml', context)