# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askbot', '0013_auto_20160607_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='offering',
        ),
        migrations.AddField(
            model_name='thread',
            name='offering',
            field=models.ForeignKey(default=0, to='askbot.Offering'),
            preserve_default=False,
        ),
    ]
