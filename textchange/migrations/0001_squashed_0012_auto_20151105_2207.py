# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'textchange', '0001_initial'), (b'textchange', '0002_auto_20150922_2307'), (b'textchange', '0003_textbook_semester'), (b'textchange', '0004_posting_class_name'), (b'textchange', '0005_remove_posting_class_name'), (b'textchange', '0006_feedback'), (b'textchange', '0007_auto_20151105_2104'), (b'textchange', '0008_auto_20151105_2107'), (b'textchange', '0009_myuser'), (b'textchange', '0010_auto_20151105_2125'), (b'textchange', '0011_myuser'), (b'textchange', '0012_auto_20151105_2207')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
        migrations.AlterUniqueTogether(
            name='textbook',
            unique_together=set([('isbn', 'class_name')]),
        ),
        migrations.AddField(
            model_name='textbook',
            name='semester',
            field=models.CharField(default=b'FALL2015', max_length=200),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='posting',
            name='image',
            field=models.ImageField(default=b'../../static/textchange/nophoto.png', upload_to=b'postingpics/%Y/%m/%d'),
        ),
    ]
