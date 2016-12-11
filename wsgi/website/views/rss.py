__author__ = 'adonis'


from website.models import NewsArticle, GalleryArticle, EducationalArticle, NewsLetter, \
    VideoArticle
from django.shortcuts import render
from django.http import Http404


def rss_index(request):
    return rss_limit(request)


def rss_limit(request, count=None):
    count = int(count) if count else None
    news_article_list = NewsArticle.objects.published(request.production).order_by('-pub_date')[:count]
    gallery_article_list = GalleryArticle.objects.published(request.production).order_by('-pub_date')[:count]
    educational_article_list = EducationalArticle.objects.published(request.production).order_by('-pub_date')[:count]
    video_article_list = VideoArticle.objects.published(request.production).order_by('-pub_date')[:count]
    newsletter_article_list = NewsLetter.objects.published(request.production).order_by('-pub_date')[:count]
    article_list = sorted(
        list(news_article_list) + list(gallery_article_list) + list(video_article_list)
        + list(educational_article_list) + list(newsletter_article_list),
        key=lambda x: x.pub_date,
        reverse=True
    )[:count]
    context = {
        'article_list': article_list
    }
    return render(request, 'website/rss/index.xml', context)


def rss_feed(request, feed):
    return rss_feed_limit(request, feed)


def rss_feed_limit(request, feed, count=None):
    count = int(count) if count else None
    feed = feed.lower()
    if feed == 'photos':
        return photos_xml(request, count)
    elif feed == 'education':
        return education_xml(request, count)
    elif feed == 'news':
        return news_xml(request, count)
    elif feed == 'newsletter':
        return newsletter_xml(request, count)
    elif feed == 'videos':
        return videos_xml(request, count)
    else:
        raise Http404


def photos_xml(request, count=None):
    article_list = GalleryArticle.objects.published(request.production).order_by('-pub_date')[:count]
    context = {
        'article_list': article_list
    }
    return render(request, 'website/rss/photos.xml', context)


def videos_xml(request, count=None):
    article_list = VideoArticle.objects.published(request.production).order_by('-pub_date')[:count]
    context = {
        'article_list': article_list
    }
    return render(request, 'website/rss/video.xml')


def education_xml(request, count=None):
    article_list = EducationalArticle.objects.published(request.production).order_by('-pub_date')[:count]
    context = {
        'article_list': article_list
    }
    return render(request, 'website/rss/education.xml', context)


def news_xml(request, count=None):
    article_list = NewsArticle.objects.published(request.production).order_by('-pub_date')[:count]
    context = {
        'article_list': article_list
    }
    return render(request, 'website/rss/news.xml', context)


def newsletter_xml(request, count=None):
    article_list = NewsLetter.objects.published(request.production).order_by('-pub_date')[:count]
    context = {
        'article_list': article_list
    }
    return render(request, 'website/rss/newsletter.xml', context)