# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textchange', '0016_statistics'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Statistics',
        ),
    ]
