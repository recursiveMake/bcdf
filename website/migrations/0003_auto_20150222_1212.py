# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150222_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='alertcampaign',
            name='article_namespace',
            field=models.CharField(max_length=64, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alertcampaign',
            name='article_slug',
            field=models.CharField(max_length=64, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bannercampaign',
            name='article_namespace',
            field=models.CharField(max_length=64, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bannercampaign',
            name='article_slug',
            field=models.CharField(max_length=64, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calendarcampaign',
            name='article_namespace',
            field=models.CharField(max_length=64, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calendarcampaign',
            name='article_slug',
            field=models.CharField(max_length=64, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepagecampaign',
            name='article_namespace',
            field=models.CharField(max_length=64, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepagecampaign',
            name='article_slug',
            field=models.CharField(max_length=64, blank=True),
            preserve_default=True,
        ),
    ]
