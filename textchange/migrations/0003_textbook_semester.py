# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0002_auto_20150922_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='textbook',
            name='semester',
            field=models.CharField(default=b'FALL2015', max_length=200),
        ),
    ]
