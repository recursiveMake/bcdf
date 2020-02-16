# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20161211_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoarticle',
            name='video_url',
            field=models.CharField(default=b'https://www.youtube.com/embed/WmERztRWLEk', max_length=256),
            preserve_default=True,
        ),
    ]
