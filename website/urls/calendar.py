__author__ = 'adonis'


from django.conf.urls import url
from website import views


urlpatterns = [
    #/calendar/
    url(r'^$', views.calendar_index, name='index')
]
