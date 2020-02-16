__author__ = 'adonis'


from django.conf.urls import url
from website import views
from website.urls.app_name import app_name

urlpatterns = [
    # /newsletter/
    # .../newsletter/
    url(r'^$', views.news_newsletter, name='index'),

    # /newsletter/2/
    url(r'^(?P<issue>\d{1,2})$', views.news_newsletter_by_issue, name='issue'),

    # /newsletter/2009/
    url(r'^(?P<year>\d{4})/$', views.news_newsletter_by_year, name='year'),

    # /news/newsletter/2009/2/
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.news_newsletter_by_month, name='month'),

    # /newsletter/slug
    url(r'^(?P<article_id>[A-Za-z0-9_\-]+)$', views.news_newsletter_by_slug, name='article'),
]
