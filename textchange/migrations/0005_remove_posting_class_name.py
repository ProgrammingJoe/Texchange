# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0004_posting_class_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posting',
            name='class_name',
        ),
    ]
