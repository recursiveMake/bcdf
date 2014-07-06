__author__ = 'adonis'

from django.conf.urls import patterns, url
from website import views

urlpatterns = patterns('',
    # /newsletter/
    url(r'^newsletter/$', views.news_newsletter, name='newsletter'),

    # /newsletter/2/
    url(r'^newsletter/(?P<issue>\d{1,2})/$', views.news_newsletter_by_issue, name='newsletter_issue'),

    # /newsletter/2009/
    url(r'^newsletter/(?P<year>\d{4})/$', views.news_newsletter_by_year, name='newsletter_year'),

    # /newsletter/2009/2/
    url(r'^newsletter/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.news_newsletter_by_month, name='newsletter_month'),

    # /about/
    url(r'^(about)/$', views.special_article, name='about'),

    # /calendar/
    url(r'^(calendar)/$', views.special_article, name='calendar'),

    # /contact/
    url(r'^contact/$', views.contact_form, name='contact'),

    # /funding/
    url(r'^(funding)/$', views.special_article, name='funding'),

    # /donate/
    url(r'^(donate)/$', views.special_article, name='donate'),

    # /news.xml
    url(r'^news.xml$', views.rss_limit, {'count': 10}, name='newsxml'),

    # /education.xml
    url(r'^education.xml$', views.education_xml, {'count': 10}, name='educationxml'),

    # /photos.xml
    url(r'^photos.xml$', views.photos_xml, name='photosxml')
)