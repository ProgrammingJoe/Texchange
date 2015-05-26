# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0004_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='wish_date',
            field=models.DateTimeField(verbose_name='date_wish'),
        ),
    ]
