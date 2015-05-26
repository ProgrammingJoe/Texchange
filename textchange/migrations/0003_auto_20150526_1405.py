# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0002_posting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='condition',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='posting',
            name='post_date',
            field=models.DateTimeField(verbose_name='date_posted'),
        ),
        migrations.AlterField(
            model_name='posting',
            name='price',
            field=models.CharField(max_length=200, default=2),
            preserve_default=False,
        ),
    ]
