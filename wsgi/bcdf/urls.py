from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bcdf.views.home', name='home'),
    # url(r'^bcdf/', include('bcdf.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', include('website.urls.home', namespace="home")),
    url(r'^news/', include('website.urls.news', namespace="news")),
    url(r'^education/', include('website.urls.education', namespace="education")),
    url(r'^rss/', include('website.urls.rss', namespace="rss")),
    url(r'^gallery/', include('website.urls.gallery', namespace="gallery")),
    url(r'^', include('website.urls.special', namespace="special")),
)