from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
import website

# Uncomment the next two lines to enable the admin:
if settings.DEPLOY:
    from django.contrib import admin
    admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', include('website.urls.home', namespace="home")),
    url(r'^news/', include('website.urls.news', namespace="news")),
    url(r'^education/', include('website.urls.education', namespace="education")),
    url(r'^rss/', include('website.urls.rss', namespace="rss")),
    url(r'^gallery/', include('website.urls.gallery', namespace="gallery")),
    url(r'^video/', include('website.urls.video', namespace="video")),
    url(r'^newsletter/', include('website.urls.newsletter', namespace='newsletter')),
    url(r'^calendar/', include('website.urls.calendar', namespace='calendar')),
    url(r'^sitemap\.xml', include('website.urls.sitemap', namespace='sitemap')),
    url(r'^', include('website.urls.special', namespace="special")),
)

if settings.DEPLOY:
    urlpatterns += patterns('',
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        url(r'^admin/', include(admin.site.urls)),
    )


handler404 = website.views.handle404

handler500 = website.views.handle500

if not settings.ON_AWS:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
