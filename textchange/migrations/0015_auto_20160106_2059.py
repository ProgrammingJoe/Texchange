# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0014_posting_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='comments',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='posting',
            name='image',
            field=models.ImageField(default=b'/textchange/nophoto.png', upload_to=b'postingpics/%Y/%m/%d'),
        ),
    ]
