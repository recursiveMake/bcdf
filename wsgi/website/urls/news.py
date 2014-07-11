__author__ = 'adonis'

from django.conf.urls import patterns, url, include
from website import views

urlpatterns = patterns('',
    # /news/
    url(r'^$', views.news_index, name='index'),

    # /news/2009/
    url(r'^(?P<year>\d{4})/$', views.news_index_by_year, name='year_index'),

    # /news/newsletter/
    url(r'^newsletter/', include('website.urls.newsletter', namespace='newsletter')),

    # /news/slug
    url(r'^(?P<article_id>[A-Za-z0-9\-_]+)$', views.news_article, name='article'),
)