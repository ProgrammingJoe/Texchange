# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0008_auto_20150805_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posting',
            name='isbn',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='isbn',
        ),
    ]
