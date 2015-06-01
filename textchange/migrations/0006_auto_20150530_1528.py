# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0005_auto_20150526_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='post_date',
            field=models.DateTimeField(verbose_name='date_posted', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='wish_date',
            field=models.DateTimeField(verbose_name='date_wish', auto_now_add=True),
        ),
    ]
