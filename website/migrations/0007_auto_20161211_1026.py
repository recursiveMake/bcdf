# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20150328_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('title', models.CharField(max_length=256)),
                ('author', models.CharField(max_length=128)),
                ('pub_date', models.DateField(verbose_name=b'date published')),
                ('is_published', models.BooleanField(default=False)),
                ('type', models.CharField(default=b'VD', max_length=2, choices=[(b'NE', b'News Article'), (b'ED', b'Educational Article'), (b'GL', b'Gallery Article'), (b'SP', b'Special Article'), (b'NL', b'Newsletter'), (b'IM', b'Image'), (b'VD', b'Video'), (b'UN', b'Unknown Type')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='articlecontent',
            name='video_article',
            field=models.OneToOneField(null=True, blank=True, on_delete=models.SET_NULL, to='website.VideoArticle'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thumb',
            name='video_article',
            field=models.OneToOneField(null=True, blank=True, on_delete=models.SET_NULL, to='website.VideoArticle'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alertcampaign',
            name='is_published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bannercampaign',
            name='is_published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='calendarcampaign',
            name='is_published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='educationalarticle',
            name='is_published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='educationalarticle',
            name='type',
            field=models.CharField(default=b'ED', max_length=2, choices=[(b'NE', b'News Article'), (b'ED', b'Educational Article'), (b'GL', b'Gallery Article'), (b'SP', b'Special Article'), (b'NL', b'Newsletter'), (b'IM', b'Image'), (b'VD', b'Video'), (b'UN', b'Unknown Type')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='galleryarticle',
            name='is_published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='galleryarticle',
            name='type',
            field=models.CharField(default=b'GL', max_length=2, choices=[(b'NE', b'News Article'), (b'ED', b'Educational Article'), (b'GL', b'Gallery Article'), (b'SP', b'Special Article'), (b'NL', b'Newsletter'), (b'IM', b'Image'), (b'VD', b'Video'), (b'UN', b'Unknown Type')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(upload_to=b'images/gallery'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepagecampaign',
            name='is_published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=b'images/full_size'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='is_published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='type',
            field=models.CharField(default=b'NE', max_length=2, choices=[(b'NE', b'News Article'), (b'ED', b'Educational Article'), (b'GL', b'Gallery Article'), (b'SP', b'Special Article'), (b'NL', b'Newsletter'), (b'IM', b'Image'), (b'VD', b'Video'), (b'UN', b'Unknown Type')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='is_published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='pdf',
            field=models.FileField(upload_to=b'newsletter/pdf'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='type',
            field=models.CharField(default=b'NL', max_length=2, choices=[(b'NE', b'News Article'), (b'ED', b'Educational Article'), (b'GL', b'Gallery Article'), (b'SP', b'Special Article'), (b'NL', b'Newsletter'), (b'IM', b'Image'), (b'VD', b'Video'), (b'UN', b'Unknown Type')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='specialarticle',
            name='is_published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='specialarticle',
            name='type',
            field=models.CharField(default=b'SP', max_length=2, choices=[(b'NE', b'News Article'), (b'ED', b'Educational Article'), (b'GL', b'Gallery Article'), (b'SP', b'Special Article'), (b'NL', b'Newsletter'), (b'IM', b'Image'), (b'VD', b'Video'), (b'UN', b'Unknown Type')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='specialimage',
            name='image',
            field=models.ImageField(upload_to=b'images/special'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thumb',
            name='image',
            field=models.ImageField(upload_to=b'images/thumbnails'),
            preserve_default=True,
        ),
    ]
