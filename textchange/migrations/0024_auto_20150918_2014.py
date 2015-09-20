# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0023_auto_20150918_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='image',
            field=models.ImageField(default=b'../../static/textchange/nophoto.jpg', upload_to=b'postingpics/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='posting',
            name='post_date',
            field=models.DateTimeField(auto_now=True, verbose_name=b'date_posted'),
        ),
    ]
