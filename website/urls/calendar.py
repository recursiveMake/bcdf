__author__ = 'adonis'


from django.conf.urls import patterns, url
from website import views


urlpatterns = patterns('',
    #/calendar/
    url(r'^$', views.calendar_index, name='index')
    )
