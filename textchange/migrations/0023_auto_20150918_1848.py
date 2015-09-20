# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0022_myuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='image',
            field=models.ImageField(default=b'../../static/textchange/nophoto.jpg', upload_to=b'postingpics/%y/%m/%d'),
        ),
    ]
