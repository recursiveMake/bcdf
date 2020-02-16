# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlertCampaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('expiry', models.DateField(null=True, blank=True)),
                ('article', models.CharField(max_length=256)),
                ('slug', models.CharField(unique=True, max_length=64)),
                ('blurb', models.CharField(max_length=512)),
                ('snooze_short', models.IntegerField(default=1)),
                ('snooze_long', models.IntegerField(default=7)),
                ('click_text', models.CharField(default=b'Click here.', max_length=32)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blurb', models.CharField(max_length=512)),
                ('short', models.TextField()),
                ('end', models.CharField(max_length=512, blank=True)),
                ('full', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'files')),
                ('blurb', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BannerCampaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('expiry', models.DateField(null=True, blank=True)),
                ('article', models.CharField(max_length=256)),
                ('slug', models.CharField(unique=True, max_length=64)),
                ('blurb', models.CharField(max_length=512)),
                ('button_text', models.CharField(default=b'Read on', max_length=32)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CalendarCampaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('expiry', models.DateField(null=True, blank=True)),
                ('article', models.CharField(max_length=256)),
                ('slug', models.CharField(unique=True, max_length=64)),
                ('blurb', models.TextField(null=True)),
                ('recurring', models.BooleanField(default=False)),
                ('link', models.CharField(max_length=64)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EducationalArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('title', models.CharField(max_length=256)),
                ('author', models.CharField(max_length=128)),
                ('pub_date', models.DateField(verbose_name=b'date published')),
                ('type', models.CharField(default=b'ED', max_length=2, choices=[(b'NE', b'News Article'), (b'ED', b'Educational Article'), (b'GL', b'Gallery Article'), (b'SP', b'Special Article'), (b'NL', b'Newsletter'), (b'IM', b'Image'), (b'UN', b'Unknown Type')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GalleryArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('title', models.CharField(max_length=256)),
                ('author', models.CharField(max_length=128)),
                ('pub_date', models.DateField(verbose_name=b'date published')),
                ('type', models.CharField(default=b'GL', max_length=2, choices=[(b'NE', b'News Article'), (b'ED', b'Educational Article'), (b'GL', b'Gallery Article'), (b'SP', b'Special Article'), (b'NL', b'Newsletter'), (b'IM', b'Image'), (b'UN', b'Unknown Type')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'images\\gallery')),
                ('description', models.CharField(max_length=512, blank=True)),
                ('alt', models.CharField(max_length=64, blank=True)),
                ('article', models.ForeignKey(on_delete=models.CASCADE, to='website.GalleryArticle')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HomePageCampaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('expiry', models.DateField(null=True, blank=True)),
                ('article', models.CharField(max_length=256)),
                ('slug', models.CharField(unique=True, max_length=64)),
                ('blurb', models.CharField(max_length=512)),
                ('button_text', models.CharField(default=b'Read on', max_length=32)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(default=b'L', max_length=1, choices=[(b'L', b'Left Justified'), (b'R', b'Right Justified'), (b'C', b'Centered')])),
                ('title', models.CharField(max_length=256, blank=True)),
                ('alt', models.CharField(max_length=256, blank=True)),
                ('description', models.CharField(max_length=512, blank=True)),
                ('image', models.ImageField(upload_to=b'images\\full_size')),
                ('banner_campaign', models.OneToOneField(null=True, blank=True, on_delete=models.SET_NULL, to='website.BannerCampaign')),
                ('educational_article', models.OneToOneField(null=True, blank=True, on_delete=models.SET_NULL, to='website.EducationalArticle')),
                ('home_page_campaign', models.OneToOneField(null=True, blank=True, on_delete=models.SET_NULL, to='website.HomePageCampaign')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('title', models.CharField(max_length=256)),
                ('author', models.CharField(max_length=128)),
                ('pub_date', models.DateField(verbose_name=b'date published')),
                ('type', models.CharField(default=b'NE', max_length=2, choices=[(b'NE', b'News Article'), (b'ED', b'Educational Article'), (b'GL', b'Gallery Article'), (b'SP', b'Special Article'), (b'NL', b'Newsletter'), (b'IM', b'Image'), (b'UN', b'Unknown Type')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('title', models.CharField(max_length=256)),
                ('author', models.CharField(max_length=128)),
                ('pub_date', models.DateField(verbose_name=b'date published')),
                ('type', models.CharField(default=b'NL', max_length=2, choices=[(b'NE', b'News Article'), (b'ED', b'Educational Article'), (b'GL', b'Gallery Article'), (b'SP', b'Special Article'), (b'NL', b'Newsletter'), (b'IM', b'Image'), (b'UN', b'Unknown Type')])),
                ('pdf', models.FileField(upload_to=b'newsletter\\pdf')),
                ('issue_number', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpecialArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('title', models.CharField(max_length=256)),
                ('author', models.CharField(max_length=128)),
                ('pub_date', models.DateField(verbose_name=b'date published')),
                ('type', models.CharField(default=b'SP', max_length=2, choices=[(b'NE', b'News Article'), (b'ED', b'Educational Article'), (b'GL', b'Gallery Article'), (b'SP', b'Special Article'), (b'NL', b'Newsletter'), (b'IM', b'Image'), (b'UN', b'Unknown Type')])),
                ('template', models.CharField(default=b'ST', max_length=2, choices=[(b'ST', b'Standard Article'), (b'MI', b'Multiple Image Article')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpecialImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'images\\special')),
                ('title', models.CharField(max_length=128, blank=True)),
                ('description', models.CharField(max_length=1024, blank=True)),
                ('alt', models.CharField(max_length=64, blank=True)),
                ('educational_article', models.ForeignKey(on_delete=models.SET_NULL, blank=True, to='website.EducationalArticle', null=True)),
                ('special_article', models.ForeignKey(on_delete=models.SET_NULL, blank=True, to='website.SpecialArticle', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Thumb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(default=b'L', max_length=1, choices=[(b'L', b'Left Justified'), (b'R', b'Right Justified'), (b'C', b'Centered')])),
                ('title', models.CharField(max_length=256, blank=True)),
                ('alt', models.CharField(max_length=256, blank=True)),
                ('description', models.CharField(max_length=512, blank=True)),
                ('image', models.ImageField(upload_to=b'images\\thumbnails')),
                ('educational_article', models.OneToOneField(null=True, blank=True, on_delete=models.SET_NULL, to='website.EducationalArticle')),
                ('gallery_article', models.OneToOneField(null=True, blank=True, on_delete=models.SET_NULL, to='website.GalleryArticle')),
                ('news_article', models.OneToOneField(null=True, blank=True, on_delete=models.SET_NULL, to='website.NewsArticle')),
                ('newsletter', models.OneToOneField(null=True, blank=True, on_delete=models.SET_NULL, to='website.NewsLetter')),
                ('special_article', models.OneToOneField(null=True, blank=True, on_delete=models.SET_NULL, to='website.SpecialArticle')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='news_article',
            field=models.OneToOneField(null=True, blank=True, on_delete=models.SET_NULL, to='website.NewsArticle'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='special_article',
            field=models.OneToOneField(null=True, blank=True, on_delete=models.SET_NULL, to='website.SpecialArticle'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articlefile',
            name='educational_article',
            field=models.ForeignKey(on_delete=models.SET_NULL, blank=True, to='website.EducationalArticle', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articlefile',
            name='news_article',
            field=models.ForeignKey(on_delete=models.SET_NULL, blank=True, to='website.NewsArticle', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articlefile',
            name='special_article',
            field=models.ForeignKey(on_delete=models.SET_NULL, blank=True, to='website.SpecialArticle', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articlecontent',
            name='educational_article',
            field=models.OneToOneField(null=True, blank=True, on_delete=models.SET_NULL, to='website.EducationalArticle'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articlecontent',
            name='gallery_article',
            field=models.OneToOneField(null=True, blank=True, on_delete=models.SET_NULL, to='website.GalleryArticle'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articlecontent',
            name='news_article',
            field=models.OneToOneField(null=True, blank=True, on_delete=models.SET_NULL, to='website.NewsArticle'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articlecontent',
            name='special_article',
            field=models.OneToOneField(null=True, blank=True, on_delete=models.SET_NULL, to='website.SpecialArticle'),
            preserve_default=True,
        ),
    ]
