# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20150222_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alertcampaign',
            name='article',
        ),
        migrations.RemoveField(
            model_name='bannercampaign',
            name='article',
        ),
        migrations.RemoveField(
            model_name='calendarcampaign',
            name='article',
        ),
        migrations.RemoveField(
            model_name='calendarcampaign',
            name='link',
        ),
        migrations.RemoveField(
            model_name='homepagecampaign',
            name='article',
        ),
    ]
