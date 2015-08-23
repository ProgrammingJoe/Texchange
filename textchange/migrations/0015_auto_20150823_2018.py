# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0014_auto_20150822_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='price',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
    ]
