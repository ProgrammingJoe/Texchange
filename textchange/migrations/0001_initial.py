# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Textbook',
            fields=[
                ('textbook_name', models.CharField(max_length=200)),
                ('class_name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('wishlist_count', models.CharField(max_length=200)),
                ('listing_count', models.CharField(max_length=200)),
            ],
        ),
    ]
