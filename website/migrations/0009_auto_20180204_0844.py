# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-04 08:44


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_videoarticle_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='alertcampaign',
            name='priority',
            field=models.PositiveSmallIntegerField(default=3),
        ),
        migrations.AddField(
            model_name='bannercampaign',
            name='priority',
            field=models.PositiveSmallIntegerField(default=3),
        ),
        migrations.AddField(
            model_name='calendarcampaign',
            name='priority',
            field=models.PositiveSmallIntegerField(default=3),
        ),
        migrations.AddField(
            model_name='homepagecampaign',
            name='priority',
            field=models.PositiveSmallIntegerField(default=3),
        ),
    ]
