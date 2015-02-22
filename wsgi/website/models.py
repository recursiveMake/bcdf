from django.db import models
import os


# Create your models here.
class Document(models.Model):
    NEWS = 'NE'
    NEWSLETTER = 'NL'
    EDUCATION = 'ED'
    SPECIAL = 'SP'
    GALLERY = 'GL'
    IMAGE = 'IM'
    UNKNOWN = 'UN'
    DocumentTypes = (
        (NEWS, 'News Article'),
        (EDUCATION, 'Educational Article'),
        (GALLERY, 'Gallery Article'),
        (SPECIAL, 'Special Article'),
        (NEWSLETTER, 'Newsletter'),
        (IMAGE, 'Image'),
        (UNKNOWN, 'Unknown Type')
    )
    slug = models.SlugField(max_length=64, unique=True)
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=128)
    pub_date = models.DateField('date published')

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title


class Campaign(models.Model):
    title = models.CharField(max_length=256)
    expiry = models.DateField(blank=True, null=True)
    article_namespace = models.CharField(max_length=64, blank=True)
    article_slug = models.CharField(max_length=64, blank=True)
    article = models.CharField(max_length=256)
    slug = models.CharField(max_length=64, unique=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title


class ImageBase(models.Model):
    LEFT = 'L'
    RIGHT = 'R'
    CENTER = 'C'
    ImagePositions = (
        (LEFT, 'Left Justified'),
        (RIGHT, 'Right Justified'),
        (CENTER, 'Centered')
    )
    position = models.CharField(max_length=1, choices=ImagePositions, default=LEFT)
    title = models.CharField(max_length=256, blank=True)
    alt = models.CharField(max_length=256, blank=True)
    description = models.CharField(max_length=512, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title


class BannerCampaign(Campaign):
    blurb = models.CharField(max_length=512)
    button_text = models.CharField(max_length=32, default='Read on')


class AlertCampaign(Campaign):
    blurb = models.CharField(max_length=512)
    snooze_short = models.IntegerField(default=1)
    snooze_long = models.IntegerField(default=7)
    click_text = models.CharField(max_length=32, default='Click here.')


class CalendarCampaign(Campaign):
    blurb = models.TextField(blank=True)
    recurring = models.BooleanField(default=False)
    link = models.CharField(max_length=64)

'''
class TipCampaign(Campaign):
    blurb = models.CharField(max_length=1024)
'''


class HomePageCampaign(Campaign):
    blurb = models.CharField(max_length=512)
    button_text = models.CharField(max_length=32, default='Read on')


class NewsLetter(Document):
    type = models.CharField(max_length=2, choices=Document.DocumentTypes, default=Document.NEWSLETTER)
    pdf = models.FileField(upload_to=os.path.join('newsletter', 'pdf'))
    issue_number = models.IntegerField()


class NewsArticle(Document):
    type = models.CharField(max_length=2, choices=Document.DocumentTypes, default=Document.NEWS)


class EducationalArticle(Document):
    type = models.CharField(max_length=2, choices=Document.DocumentTypes, default=Document.EDUCATION)


class GalleryArticle(Document):
    type = models.CharField(max_length=2, choices=Document.DocumentTypes, default=Document.GALLERY)


class SpecialArticle(Document):
    STANDARD = 'ST'
    MULTI_IMAGE = 'MI'
    SpecialTypes = (
        (STANDARD, 'Standard Article'),
        (MULTI_IMAGE, 'Multiple Image Article'),
    )
    type = models.CharField(max_length=2, choices=Document.DocumentTypes, default=Document.SPECIAL)
    template = models.CharField(max_length=2, choices=SpecialTypes, default=STANDARD)


class SpecialImage(models.Model):
    ''' Multiple image article, also used in Educational Articles
    '''
    special_article = models.ForeignKey(SpecialArticle, blank=True, null=True)
    educational_article = models.ForeignKey(EducationalArticle, blank=True, null=True)

    image = models.ImageField(upload_to=os.path.join("images", "special"))
    title = models.CharField(max_length=128, blank=True)
    description = models.CharField(max_length=1024, blank=True)
    alt = models.CharField(max_length=64, blank=True)


class GalleryImage(models.Model):
    article = models.ForeignKey(GalleryArticle)
    image = models.ImageField(upload_to=os.path.join('images', 'gallery'))
    description = models.CharField(max_length=512, blank=True)
    alt = models.CharField(max_length=64, blank=True)

    def __unicode__(self):
        return self.description or 'GalleryImage Object'


class Image(ImageBase):
    image = models.ImageField(upload_to=os.path.join('images', 'full_size'))

    banner_campaign = models.OneToOneField(BannerCampaign, blank=True, null=True)
    home_page_campaign = models.OneToOneField(HomePageCampaign, blank=True, null=True)
    news_article = models.OneToOneField(NewsArticle, blank=True, null=True)
    educational_article = models.OneToOneField(EducationalArticle, blank=True, null=True)
    special_article = models.OneToOneField(SpecialArticle, blank=True, null=True)


class Thumb(ImageBase):
    image = models.ImageField(upload_to=os.path.join('images', 'thumbnails'))

    newsletter = models.OneToOneField(NewsLetter, blank=True, null=True)
    news_article = models.OneToOneField(NewsArticle, blank=True, null=True)
    educational_article = models.OneToOneField(EducationalArticle, blank=True, null=True)
    gallery_article = models.OneToOneField(GalleryArticle, blank=True, null=True)
    special_article = models.OneToOneField(SpecialArticle, blank=True, null=True)


class ArticleContent(models.Model):
    blurb = models.CharField(max_length=512)
    short = models.TextField()
    end = models.CharField(max_length=512, blank=True)
    full = models.TextField(blank=True)

    news_article = models.OneToOneField(NewsArticle, blank=True, null=True)
    educational_article = models.OneToOneField(EducationalArticle, blank=True, null=True)
    gallery_article = models.OneToOneField(GalleryArticle, blank=True, null=True)
    special_article = models.OneToOneField(SpecialArticle, blank=True, null=True)

    def __unicode__(self):
        return self.blurb


class ArticleFile(models.Model):
    file = models.FileField(upload_to="files")
    blurb = models.CharField(max_length=256)

    educational_article = models.ForeignKey(EducationalArticle, blank=True, null=True)
    news_article = models.ForeignKey(NewsArticle, blank=True, null=True)
    special_article = models.ForeignKey(SpecialArticle, blank=True, null=True)