__author__ = 'adonis'

from django import forms
from django.contrib import admin
from django.urls import reverse, NoReverseMatch
from website.models import ArticleContent, ArticleFile, Thumb, Image, GalleryImage, SpecialImage, \
    VideoArticle
from website.models import EducationalArticle, NewsArticle, GalleryArticle, NewsLetter, SpecialArticle
from website.models import BannerCampaign, AlertCampaign, HomePageCampaign, CalendarCampaign


class SpecialMultiImageInline(admin.StackedInline):
    model = SpecialImage
    exclude = ('educational_article', )
    extra = 4


class SpecialImageInline(admin.StackedInline):
    model = Image
    exclude = ('banner_campaign', 'home_page_campaign', 'educational_article', 'news_article')
    extra = 1


class SpecialThumbInline(admin.StackedInline):
    model = Thumb
    exclude = ('newsletter', 'news_article', 'educational_article', 'gallery_article', 'video_article')
    extra = 1


class SpecialContentInline(admin.StackedInline):
    model = ArticleContent
    exclude = ('news_article', 'educational_article', 'gallery_article', 'video_article')
    extra = 1


class SpecialFileInline(admin.StackedInline):
    model = ArticleFile
    exclude = ('news_article', 'educational_article')
    extra = 1


class SpecialArticleAdmin(admin.ModelAdmin):
    inlines = [SpecialContentInline, SpecialThumbInline, SpecialImageInline, SpecialMultiImageInline, SpecialFileInline]
    exclude = ('type', )


class GalleryImageInline(admin.StackedInline):
    model = GalleryImage
    extra = 4


class GalleryThumbInline(admin.StackedInline):
    model = Thumb
    exclude = ('newsletter', 'news_article', 'educational_article', 'special_article', 'video_article')
    extra = 1


class GalleryContentInline(admin.StackedInline):
    model = ArticleContent
    exclude = ('news_article', 'educational_article', 'special_article', 'video_article')
    extra = 1


class GalleryArticleAdmin(admin.ModelAdmin):
    inlines = [GalleryContentInline, GalleryThumbInline, GalleryImageInline]
    exclude = ('type', )


class CampaignAdminForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(CampaignAdminForm, self).clean()
        namespace = cleaned_data.get('article_namespace')
        slug = cleaned_data.get('article_slug')
        if slug:
            try:
                reverse(namespace, args=(slug, ))
            except NoReverseMatch:
                raise forms.ValidationError('No reverse match for slug')
        else:
            try:
                reverse(namespace)
            except NoReverseMatch:
                raise forms.ValidationError('No reverse match for namespace')


class HomePageImageInline(admin.StackedInline):
    model = Image
    exclude = ('banner_campaign', 'news_article', 'educational_article', 'special_article')
    extra = 1


class HomePageCampaignAdmin(admin.ModelAdmin):
    inlines = [HomePageImageInline]
    form = CampaignAdminForm


class BannerImageInline(admin.StackedInline):
    model = Image
    exclude = ('news_article', 'home_page_campaign', 'educational_article', 'special_article')
    extra = 1


class BannerCampaignAdmin(admin.ModelAdmin):
    inlines = [BannerImageInline]
    form = CampaignAdminForm


class AlertCampaignAdmin(admin.ModelAdmin):
    form = CampaignAdminForm


class CalendarCampaignAdmin(admin.ModelAdmin):
    form = CampaignAdminForm


class NewsThumbInline(admin.StackedInline):
    model = Thumb
    exclude = ('newsletter', 'gallery_article', 'educational_article', 'special_article', 'video_article')
    extra = 1


class NewsImageInline(admin.StackedInline):
    model = Image
    exclude = ('banner_campaign', 'home_page_campaign', 'educational_article', 'special_article')
    extra = 1


class NewsArticleContentInline(admin.StackedInline):
    model = ArticleContent
    exclude = ('gallery_article', 'educational_article', 'special_article', 'video_article')
    extra = 1


class NewsArticleFileInline(admin.StackedInline):
    model = ArticleFile
    exclude = ('special_article', 'educational_article')
    extra = 1


class NewsArticleAdmin(admin.ModelAdmin):
    inlines = [NewsArticleContentInline, NewsImageInline, NewsThumbInline, NewsArticleFileInline]
    exclude = ('type', )


class VideoThumbInline(admin.StackedInline):
    model = Thumb
    exclude = ('newsletter', 'gallery_article', 'educational_article', 'special_article', 'news_article')
    extra = 1


class VideoArticleContentInline(admin.StackedInline):
    model = ArticleContent
    exclude = ('gallery_article', 'educational_article', 'special_article', 'news_article')
    extra = 1


class VideoArticleAdmin(admin.ModelAdmin):
    inlines = [VideoArticleContentInline, VideoThumbInline]
    exclude = ('type', )


class EducationalThumbInline(admin.StackedInline):
    model = Thumb
    exclude = ('newsletter', 'news_article', 'gallery_article', 'special_article', 'video_article')
    extra = 1


class EducationalImageInline(admin.StackedInline):
    model = Image
    exclude = ('banner_campaign', 'news_article', 'home_page_campaign', 'special_article')
    extra = 1


class EducationalMultiImageInline(admin.StackedInline):
    model = SpecialImage
    exclude = ('special_article', )
    extra = 1


class EducationalArticleContentInline(admin.StackedInline):
    model = ArticleContent
    exclude = ('news_article', 'gallery_article', 'special_article', 'video_article')
    extra = 1


class EducationalArticleFileInline(admin.StackedInline):
    model = ArticleFile
    exclude = ('news_article', 'special_article')
    extra = 1


class EducationalArticleAdmin(admin.ModelAdmin):
    inlines = [EducationalArticleContentInline, EducationalImageInline, EducationalThumbInline,
               EducationalArticleFileInline, EducationalMultiImageInline]
    exclude = ('type', )


class NewsLetterThumbInline(admin.StackedInline):
    model = Thumb
    exclude = ('news_article', 'gallery_article', 'educational_article', 'special_article', 'video_article')


class NewsLetterAdmin(admin.ModelAdmin):
    inlines = [NewsLetterThumbInline]
    exclude = ('type',)


admin.site.register(NewsArticle, NewsArticleAdmin)

admin.site.register(NewsLetter, NewsLetterAdmin)

admin.site.register(EducationalArticle, EducationalArticleAdmin)

admin.site.register(GalleryArticle, GalleryArticleAdmin)

admin.site.register(SpecialArticle, SpecialArticleAdmin)

admin.site.register(BannerCampaign, BannerCampaignAdmin)

admin.site.register(AlertCampaign, AlertCampaignAdmin)

admin.site.register(CalendarCampaign, CalendarCampaignAdmin)

admin.site.register(HomePageCampaign, HomePageCampaignAdmin)

admin.site.register(VideoArticle, VideoArticleAdmin)
