from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
import website

# Uncomment the next two lines to enable the admin:
if settings.DEPLOY:
    from django.contrib import admin
    admin.autodiscover()


urlpatterns = [
    re_path(r'^', include('website.urls.home', namespace="home")),
    re_path(r'^news/', include('website.urls.news', namespace="news")),
    re_path(r'^education/', include('website.urls.education', namespace="education")),
    re_path(r'^rss/', include('website.urls.rss', namespace="rss")),
    re_path(r'^gallery/', include('website.urls.gallery', namespace="gallery")),
    re_path(r'^video/', include('website.urls.video', namespace="video")),
    re_path(r'^newsletter/', include('website.urls.newsletter', namespace='newsletter')),
    re_path(r'^calendar/', include('website.urls.calendar', namespace='calendar')),
    re_path(r'^sitemap\.xml', include('website.urls.sitemap', namespace='sitemap')),
    re_path(r'^', include('website.urls.special', namespace="special")),
]

if settings.DEPLOY:
    urlpatterns += [
        path('admin/', admin.site.urls),
    ]


handler404 = website.views.handle404

handler500 = website.views.handle500

if not settings.ON_AWS:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
