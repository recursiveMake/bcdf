__author__ = 'adonis'


from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from website.models import NewsArticle, EducationalArticle, GalleryArticle, SpecialArticle


class NewsSiteMap(Sitemap):
    changefreq = "daily"
    priority = 0.75

    def items(self):
        return NewsArticle.objects.all()

    def lastmod(self, obj):
        return obj.pub_date

    def location(self, obj):
        return reverse('news:article', args=(obj.slug,))


class EducationSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return EducationalArticle.objects.all()

    def lastmod(self, obj):
        return obj.pub_date

    def location(self, obj):
        return reverse('education:article', args=(obj.slug,))


class GallerySiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return GalleryArticle.objects.all()

    def lastmod(self, obj):
        return obj.pub_date

    def location(self, obj):
        return reverse('gallery:article', args=(obj.slug,))


class SpecialSiteMap(Sitemap):
    changefreq = "yearly"
    priority = 0.25

    def items(self):
        return SpecialArticle.objects.all()

    def lastmod(self, obj):
        return obj.pub_date

    def location(self, obj):
        return reverse('special:' + obj.slug, args=(obj.slug,))

sitemaps = {
    'news': NewsSiteMap,
    'education': EducationSiteMap,
    'gallery': GallerySiteMap,
    'flatpages': SpecialSiteMap
}
