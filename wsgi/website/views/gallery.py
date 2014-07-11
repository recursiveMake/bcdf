__author__ = 'adonis'


from website.models import GalleryArticle
from django.shortcuts import get_object_or_404, render
from website.views.util import update_context


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

def gallery_xml(request, article_id):
    response = get_object_or_404(GalleryArticle, slug=article_id)
    context = {
        'article': response
    }
    return render(request, 'website/rss/gallery.xml', context)