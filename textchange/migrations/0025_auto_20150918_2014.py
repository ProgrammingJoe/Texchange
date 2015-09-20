# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0024_auto_20150918_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='post_date',
            field=models.DateTimeField(verbose_name=b'date_posted'),
        ),
    ]
