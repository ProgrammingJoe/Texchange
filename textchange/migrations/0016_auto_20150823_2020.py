# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0015_auto_20150823_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='price',
            field=models.CharField(max_length=200),
        ),
    ]
