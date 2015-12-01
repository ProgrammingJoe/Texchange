# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0004_auto_20151129_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(default=b'JoeCzepil', to=settings.AUTH_USER_MODEL),
        ),
    ]
