# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('askbot', '0014_auto_20160607_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='offering',
            name='professor',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='offering',
            name='term',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='offering',
            name='timings',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='offering',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 8, 12, 15, 40, 771288), auto_now_add=True),
            preserve_default=False,
        ),
    ]
