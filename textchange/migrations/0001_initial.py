# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facebook', models.CharField(max_length=300)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('condition', models.CharField(max_length=200)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('image', models.ImageField(default=b'../../static/textchange/nophoto.jpg', upload_to=b'postingpics/%Y/%m/%d')),
                ('post_date', models.DateTimeField(verbose_name=b'date_posted')),
            ],
        ),
        migrations.CreateModel(
            name='Textbook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('textbook_name', models.CharField(max_length=200)),
                ('class_name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('wish_date', models.DateTimeField(verbose_name=b'date_wish')),
                ('textbook', models.ForeignKey(to='textchange.Textbook')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='posting',
            name='textbook',
            field=models.ForeignKey(to='textchange.Textbook'),
        ),
        migrations.AddField(
            model_name='posting',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
