__author__ = 'adonis'

from django.contrib import admin
from website.models import ArticleContent, Thumb, Image, GalleryImage, SpecialImage
from website.models import EducationalArticle, NewsArticle, GalleryArticle, NewsLetter, SpecialArticle
from website.models import BannerCampaign, AlertCampaign, HomePageCampaign


class SpecialMultiImageInline(admin.StackedInline):
    model = SpecialImage
    extra = 4


class SpecialImageInline(admin.StackedInline):
    model = Image
    exclude = ('banner_campaign', 'home_page_campaign', 'educational_article', 'news_article')
    extra = 1


class SpecialThumbInline(admin.StackedInline):
    model = Thumb
    exclude = ('newsletter', 'news_article', 'educational_article', 'gallery_article')
    extra = 1


class SpecialContentInline(admin.StackedInline):
    model = ArticleContent
    exclude = ('news_article', 'educational_article', 'gallery_article')
    extra = 1


class SpecialArticleAdmin(admin.ModelAdmin):
    inlines = [SpecialContentInline, SpecialThumbInline, SpecialImageInline, SpecialMultiImageInline]
    exclude = ('type', )


class GalleryImageInline(admin.StackedInline):
    model = GalleryImage
    extra = 4


class GalleryThumbInline(admin.StackedInline):
    model = Thumb
    exclude = ('newsletter', 'news_article', 'educational_article', 'special_article')
    extra = 1


class GalleryContentInline(admin.StackedInline):
    model = ArticleContent
    exclude = ('news_article', 'educational_article', 'special_article')
    extra = 1


class GalleryArticleAdmin(admin.ModelAdmin):
    inlines = [GalleryContentInline, GalleryThumbInline, GalleryImageInline]
    exclude = ('type', )


class HomePageImageInline(admin.StackedInline):
    model = Image
    exclude = ('banner_campaign', 'news_article', 'educational_article', 'special_article')
    extra = 1


class HomePageCampaignAdmin(admin.ModelAdmin):
    inlines = [HomePageImageInline]


class BannerImageInline(admin.StackedInline):
    model = Image
    exclude = ('news_article', 'home_page_campaign', 'educational_article', 'special_article')
    extra = 1


class BannerCampaignAdmin(admin.ModelAdmin):
    inlines = [BannerImageInline]


class NewsThumbInline(admin.StackedInline):
    model = Thumb
    exclude = ('newsletter', 'gallery_article', 'educational_article', 'special_article')
    extra = 1


class NewsImageInline(admin.StackedInline):
    model = Image
    exclude = ('banner_campaign', 'home_page_campaign', 'educational_article', 'special_article')
    extra = 1


class NewsArticleContentInline(admin.StackedInline):
    model = ArticleContent
    exclude = ('gallery_article', 'educational_article', 'special_article')
    extra = 1


class NewsArticleAdmin(admin.ModelAdmin):
    inlines = [NewsArticleContentInline, NewsImageInline, NewsThumbInline]
    exclude = ('type', )

class EducationalThumbInline(admin.StackedInline):
    model = Thumb
    exclude = ('newsletter', 'news_article', 'gallery_article', 'special_article')
    extra = 1


class EducationalImageInline(admin.StackedInline):
    model = Image
    exclude = ('banner_campaign', 'news_article', 'home_page_campaign', 'special_article')
    extra = 1


class EducationalArticleContentInline(admin.StackedInline):
    model = ArticleContent
    exclude = ('news_article', 'gallery_article', 'special_article')
    extra = 1


class EducationalArticleAdmin(admin.ModelAdmin):
    inlines = [EducationalArticleContentInline, EducationalImageInline, EducationalThumbInline]
    exclude = ('type', )


class NewsLetterThumbInline(admin.StackedInline):
    model = Thumb
    exclude = ('news_article', 'gallery_article', 'educational_article', 'special_article')


class NewsLetterAdmin(admin.ModelAdmin):
    inlines = [NewsLetterThumbInline]
    exclude = ('type',)


admin.site.register(NewsArticle, NewsArticleAdmin)

admin.site.register(NewsLetter, NewsLetterAdmin)

admin.site.register(EducationalArticle, EducationalArticleAdmin)

admin.site.register(GalleryArticle, GalleryArticleAdmin)

admin.site.register(SpecialArticle, SpecialArticleAdmin)

admin.site.register(BannerCampaign, BannerCampaignAdmin)

admin.site.register(AlertCampaign)

admin.site.register(HomePageCampaign, HomePageCampaignAdmin)


