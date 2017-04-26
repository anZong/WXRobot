# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bugs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=255)),
                ('add_date', models.DateTimeField(default=datetime.datetime(2017, 4, 26, 11, 14, 56, 177000, tzinfo=utc), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xa5\xe6\x9c\x9f')),
                ('last_date', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xa5\xe6\x9c\x9f')),
                ('content', models.TextField(null=True)),
                ('img', models.ImageField(default=b'', upload_to=b'')),
                ('result', models.BooleanField(default=False)),
            ],
        ),
    ]
