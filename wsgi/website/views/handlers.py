__author__ = 'adonis'


from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from website.models import SpecialArticle
from website.views.util import article_parse


def handle404(request):
    messages.error(request, "The requested page was not found.")
    response = get_object_or_404(SpecialArticle, slug='broken-link')
    (request, context) = article_parse(request, response)
    return render(request, 'website/special/article.html', context, status=404)


def handle500(request):
    messages.error(request, "An error has occurred on the server.")
    response = get_object_or_404(SpecialArticle, slug='broken-site')
    (request, context) = article_parse(request, response)
    return render(request, 'website/special/article.html', context, status=500)
