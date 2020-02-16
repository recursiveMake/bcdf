__author__ = 'adonis'

from django.conf.urls import url
from website import views
from website.urls.app_name import app_name

urlpatterns = [
    # /gallery/
    url(r'^$', views.gallery_index, name='index'),

    # /gallery/slug
    url(r'^(?P<article_id>[A-Za-z0-9\-_]+)$', views.gallery_article, name='article'),

    # /gallery/xml/slug
    url(r'^xml/(?P<article_id>[A-Za-z0-9\-_]+)$', views.gallery_xml, name='xml')
]
