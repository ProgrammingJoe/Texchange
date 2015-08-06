# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0007_auto_20150601_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='isbn',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='isbn',
            field=models.CharField(null=True, max_length=200),
        ),
    ]
