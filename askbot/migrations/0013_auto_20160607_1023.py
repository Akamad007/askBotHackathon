# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askbot', '0012_rename_related_name_to_auth_user_from_Vote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='emailfeedsetting',
            name='frequency',
            field=models.CharField(default=b'n', max_length=8, choices=[(b'i', 'instantly'), (b'd', 'daily'), (b'w', 'weekly'), (b'n', 'never')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='primary_language',
            field=models.CharField(default=b'en', max_length=16, choices=[(b'en', b'English')]),
        ),
        migrations.AddField(
            model_name='post',
            name='offering',
            field=models.ForeignKey(default=1, to='askbot.Offering'),
            preserve_default=False,
        ),
    ]
