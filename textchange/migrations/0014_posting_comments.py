# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0013_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='comments',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
