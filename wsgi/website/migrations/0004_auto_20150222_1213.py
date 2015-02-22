# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def get_namespace_from_url(url):
    segments = url.split('/')
    namespace = segments[1] if len(segments) >= 2 else ''
    slug = segments[2] if len(segments) >= 3 else ''
    if namespace == 'news':
        if slug:
            if slug == 'newsletter':
                return 'newsletter:index', ''
            else:
                return 'news:article', slug
        else:
            return 'news:index', ''
    if namespace == 'gallery':
        if slug:
            return 'gallery:article', slug
        else:
            return 'gallery:index', ''
    if namespace == 'education':
        if slug:
            return 'education:article', slug
        else:
            return 'education:index', ''
    if namespace == 'donate':
        return 'special:donate', ''
    if namespace == 'about':
        return 'special:about', 'about'
    return '', ''


def split_article_in_campaign(apps, campaign_str):
    Campaign = apps.get_model('website', campaign_str)
    for campaign in Campaign.objects.all():
        campaign.article_namespace, campaign.article_slug = get_namespace_from_url(campaign.article)
        campaign.save()


def split_article(apps, schema_editor):
    for campaign_str in ('CalendarCampaign', 'BannerCampaign', 'AlertCampaign', 'HomePageCampaign'):
        split_article_in_campaign(apps, campaign_str)


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20150222_1212'),
    ]

    operations = [
        migrations.RunPython(split_article),
    ]
