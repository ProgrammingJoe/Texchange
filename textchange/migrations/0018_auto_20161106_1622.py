# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0017_delete_statistics'),
    ]

    operations = [
        migrations.AddField(
            model_name='textbook',
            name='longschool',
            field=models.CharField(default=b'University of Victoria', max_length=200),
        ),
        migrations.AddField(
            model_name='textbook',
            name='shortschool',
            field=models.CharField(default=b'UVic', max_length=20),
        ),
    ]
