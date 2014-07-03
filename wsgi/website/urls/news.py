__author__ = 'adonis'

from django.conf.urls import patterns, url
from website import views

urlpatterns = patterns('',
    # /news/
    url(r'^$', views.news_index, name='index'),

    # /news/2009/
    url(r'^(?P<year>\d{4})/$', views.news_index_by_year, name='year_index'),


    # /news/newsletter/
    url(r'^newsletter/$', views.news_newsletter, name='newsletter'),

    # /news/newsletter/2/
    url(r'^newsletter/(?P<issue>\d{1,2})/$', views.news_newsletter_by_issue, name='newsleter_issue'),

    # /news/newsletter/2009/
    url(r'^newsletter/(?P<year>\d{4})/$', views.news_newsletter_by_year, name='newsletter_year'),

    # /news/newsletter/2009/2/
    url(r'^newsletter/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.news_newsletter_by_month, name='newsletter_month'),

    # /news/slug
    url(r'^(?P<article_id>[A-Za-z0-9\-_]+)$', views.news_article, name='article'),

)