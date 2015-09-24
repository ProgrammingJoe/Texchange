# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0003_textbook_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='class_name',
            field=models.CharField(default=b'Test', max_length=200),
        ),
    ]
