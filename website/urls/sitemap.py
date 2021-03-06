__author__ = 'adonis'


from django.contrib.sitemaps import GenericSitemap
from django.contrib.sites.models import Site
from django.contrib.sitemaps.views import sitemap as django_sitemap
from django.urls import reverse
from django.conf import settings
from django.conf.urls import url
from django.db.models import Q
from website.models import NewsArticle, EducationalArticle, GalleryArticle, SpecialArticle, NewsLetter, \
    VideoArticle
from website.urls.app_name import app_name


class CustomSitemap(GenericSitemap):

    def __init__(self, site, namespace, *args, **kwargs):
        self.site = site
        self.namespace = namespace
        super(CustomSitemap, self).__init__(*args, **kwargs)

    def get_urls(self, page=1, site=None, protocol=None):
        protocol = 'https' if settings.ON_AWS else None
        return super(CustomSitemap, self).get_urls(page, self.site, protocol=protocol)

    def location(self, obj):
        return reverse(self.namespace, args=(obj.slug, ))


class IndexSitemap(CustomSitemap):

    def items(self):
        return ['news', 'gallery', 'education', 'newsletter', 'calendar']

    def location(self, obj):
        return reverse(obj + ':' + 'index')


class SpecialSitemap(CustomSitemap):

    def location(self, obj):
        if obj.slug in ('about', 'donate', 'funding'):
            return reverse(self.namespace + obj.slug)
        else:
            return reverse(self.namespace + 'special', args=(obj.slug, ))


def sitemap_view(request):
    index_sitemap = IndexSitemap(
        site=Site(domain=request.get_host()),
        namespace=None,
        info_dict={
            'queryset': None,
        },
        priority=1,
        changefreq="daily"
    )
    news_sitemap = CustomSitemap(
        site=Site(domain=request.get_host()),
        namespace='news:article',
        info_dict={
            'queryset': NewsArticle.objects.published(request.production).order_by('-pub_date'),
            'date_field': 'pub_date'
        },
        priority=0.75,
        changefreq="daily"
    )
    education_sitemap = CustomSitemap(
        site=Site(domain=request.get_host()),
        namespace='education:article',
        info_dict={
            'queryset': EducationalArticle.objects.published(request.production).order_by('-pub_date'),
            'date_field': 'pub_date'
        },
        priority=0.75,
        changefreq="weekly"
    )
    newsletter_sitemap = CustomSitemap(
        site=Site(domain=request.get_host()),
        namespace='newsletter:article',
        info_dict={
            'queryset': NewsLetter.objects.published(request.production).order_by('-pub_date'),
            'date_field': 'pub_date'
        },
        priority=0.75,
        changefreq="monthly"
    )
    gallery_sitemap = CustomSitemap(
        site=Site(domain=request.get_host()),
        namespace='gallery:article',
        info_dict={
            'queryset': GalleryArticle.objects.published(request.production).order_by('-pub_date'),
            'date_field': 'pub_date'
        },
        priority=0.75,
        changefreq="monthly"
    )
    video_sitemap = CustomSitemap(
        site=Site(domain=request.get_host()),
        namespace='video:article',
        info_dict={
            'queryset': VideoArticle.objects.published(request.production).order_by('-pub_date'),
            'date_field': 'pub_date'
        },
        priority=0.75,
        changefreq="monthly"
    )
    special_sitemap = SpecialSitemap(
        site=Site(domain=request.get_host()),
        namespace='special:',
        info_dict={
            'queryset': SpecialArticle.objects.filter(~Q(slug__startswith='broken-')).order_by('-pub_date'),
            'date_field': 'pub_date'
        },
        priority=0.5,
        changefreq="yearly"
    )
    sitemaps = {
        'index': index_sitemap,
        'news': news_sitemap,
        'education': education_sitemap,
        'newsletter': newsletter_sitemap,
        'gallery': gallery_sitemap,
        'video': video_sitemap,
        'flatpages': special_sitemap
    }
    return django_sitemap(request, sitemaps)


urlpatterns = [
    url(r'^$', sitemap_view, name='index'),
]
