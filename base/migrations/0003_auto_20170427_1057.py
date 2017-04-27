# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20170426_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugs',
            name='projectName',
            field=models.CharField(default=datetime.datetime(2017, 4, 27, 2, 57, 39, 866000, tzinfo=utc), max_length=255, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bugs',
            name='content',
            field=models.TextField(null=True, verbose_name=b'Bug\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='bugs',
            name='img',
            field=models.ImageField(default=b'', upload_to=b'', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='bugs',
            name='result',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\xa4\x84\xe7\x90\x86\xe6\x83\x85\xe5\x86\xb5'),
        ),
        migrations.AlterField(
            model_name='bugs',
            name='user',
            field=models.CharField(max_length=255, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7'),
        ),
    ]
