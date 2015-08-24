# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0017_auto_20150823_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textbook',
            name='listing_count',
        ),
        migrations.RemoveField(
            model_name='textbook',
            name='wishlist_count',
        ),
    ]
