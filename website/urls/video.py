from django.conf.urls import url

from website import views
from website.urls.app_name import app_name

urlpatterns = [
    # /video/
    url(r'^$', views.video_index, name='index'),

    # /video/slug
    url(r'^(?P<article_id>[A-Za-z0-9\-_]+)$', views.video_article, name='article'),

    # /video/xml/slug
    url(r'^xml/(?P<article_id>[A-Za-z0-9\-_]+)$', views.video_xml, name='xml')
]
