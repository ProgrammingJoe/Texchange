# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0020_feedback_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='image',
            field=models.ImageField(default=False, upload_to=b'postingpics/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='posting',
            name='price',
            field=models.DecimalField(max_digits=7, decimal_places=2),
        ),
    ]
