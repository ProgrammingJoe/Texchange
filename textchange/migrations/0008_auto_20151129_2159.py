# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0007_auto_20151129_2158'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserFeedback',
            new_name='Feedback',
        ),
    ]
