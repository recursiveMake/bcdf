__author__ = 'adonis'

from django.conf.urls import patterns, url
from website import views

urlpatterns = patterns('',
    # /
    url(r'^$', views.home_index, name='index'),
)