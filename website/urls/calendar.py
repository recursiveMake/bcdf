__author__ = 'adonis'


from django.conf.urls import url
from website import views
from website.urls.app_name import app_name

urlpatterns = [
    #/calendar/
    url(r'^$', views.calendar_index, name='index')
]
