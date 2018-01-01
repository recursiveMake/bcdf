__author__ = 'adonis'

from django.conf.urls import url
from website import views

urlpatterns = [
    # /rss/
    url(r'^$', views.rss_index, name='index'),

    # /rss/5
    url(r'^(?P<count>\d{1,2})$', views.rss_limit, name='index'),

    # /rss/news/
    url(r'^(?P<feed>[A-Za-z]+)/$', views.rss_feed, name='feed'),

    # /rss/news/5
    url(r'^(?P<feed>[A-Za-z]+)/(?P<count>\d{1,2})$', views.rss_feed_limit, name='feed_limit'),
]
