# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0006_auto_20150530_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='post_date',
            field=models.DateTimeField(verbose_name='date_posted'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='wish_date',
            field=models.DateTimeField(verbose_name='date_wish'),
        ),
    ]
