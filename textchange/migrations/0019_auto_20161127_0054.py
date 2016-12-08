# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0018_auto_20161106_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='textbook',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='user',
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
