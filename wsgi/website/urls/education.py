__author__ = 'adonis'


from django.conf.urls import patterns, url
from website import views

urlpatterns = patterns('',
    # /education/
    url(r'^$', views.education_index, name='index'),

    # /education/2009/
    url(r'^(?P<year>\d{4})/$', views.education_index_by_year, name='year_index'),

    # /education/slug
    url(r'^(?P<article_id>[A-Za-z0-9\-_]+)$', views.education_article, name='article'),

)
