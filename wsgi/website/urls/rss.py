__author__ = 'adonis'

from django.conf.urls import patterns, url
from website import views

urlpatterns = patterns('',
    # /rss/
    url(r'^$', views.rss_index, name='index'),

    # /rss/5
    url(r'^(?P<count>\d{1,2})$', views.rss_limit, name='index'),

)