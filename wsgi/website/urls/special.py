__author__ = 'adonis'

from django.conf.urls import patterns, url
from website import views

urlpatterns = patterns('',

    # /about/
    url(r'^about/$', views.special_article, {'article_id': 'about'}, name='about'),

    # /calendar/
    url(r'^calendar/$', views.special_article, {'article_id': 'calendar'}, name='calendar'),

    # /contact/
    url(r'^contact/$', views.contact_form, name='contact'),

    # /funding/
    url(r'^funding/$', views.special_article, {'article_id': 'funding'}, name='funding'),

    # /donate/
    url(r'^donate/$', views.special_article, {'article_id': 'donate'}, name='donate'),

    # /news.xml
    url(r'^(?P<feed>[A-Za-z]+).xml$', views.rss_feed_limit, {'count': 10}, name='rss'),

    # /news.xml/10
    url(r'^(?P<feed>[A-Za-z]+).xml/(?P<count>\d{1,2})$', views.rss_feed_limit, name='rss_limit'),
)