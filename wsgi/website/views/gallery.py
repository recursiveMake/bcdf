__author__ = 'adonis'


from website.models import GalleryArticle
from django.shortcuts import get_object_or_404
from website.views.util import render, paginate


def gallery_index(request):
    article_list = GalleryArticle.objects.all().order_by('-pub_date')
    article_list = paginate(request, article_list)
    context = {
        'article_list': article_list,
        'url_namespace': 'gallery:article',
        'read_on_message': 'View the pictures...'
    }
    return render(request, 'website/gallery/index.html', context)


def gallery_article(request, article_id):
    article = get_object_or_404(GalleryArticle, slug=article_id)
    context = {'article': article}
    return render(request, 'website/gallery/article.html', context)


def gallery_xml(request, article_id):
    response = get_object_or_404(GalleryArticle, slug=article_id)
    context = {
        'article': response
    }
    return render(request, 'website/rss/gallery.xml', context)