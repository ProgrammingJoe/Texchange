# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('textchange', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('condition', models.CharField(max_length=200, blank=True)),
                ('price', models.CharField(max_length=200, null=True)),
                ('post_date', models.DateTimeField(verbose_name='date_posted', blank=True)),
                ('textbook', models.ForeignKey(to='textchange.Textbook')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
