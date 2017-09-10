from django.shortcuts import get_object_or_404

from website.models import VideoArticle
from website.views.util import render, paginate


def video_index(request):
    article_list = VideoArticle.objects.published(request.production).order_by('-pub_date')
    article_list = paginate(request, article_list)
    context = {
        'article_list': article_list,
        'url_namespace': 'video:article',
        'read_on_message': 'View the video...'
    }
    return render(request, 'website/video/index.html', context)


def video_article(request, article_id):
    article = get_object_or_404(VideoArticle.objects.published(request.production), slug=article_id)
    context = {'article': article}
    return render(request, 'website/video/article.html', context)


def video_xml(request, article_id):
    response = get_object_or_404(VideoArticle.objects.published(request.production), slug=article_id)
    context = {
        'article': response
    }
    return render(request, 'website/rss/video.xml', context)
