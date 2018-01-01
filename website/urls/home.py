__author__ = 'adonis'

from django.conf.urls import url
from website import views

urlpatterns = [
    # /
    url(r'^$', views.home_index, name='index'),
]