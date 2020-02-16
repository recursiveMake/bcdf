# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarcampaign',
            name='blurb',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
    ]
