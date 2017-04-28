# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bugs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=255, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7')),
                ('projectName', models.CharField(max_length=255, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0')),
                ('add_date', models.DateTimeField(auto_now=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xa5\xe6\x9c\x9f')),
                ('last_date', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xa5\xe6\x9c\x9f')),
                ('content', models.TextField(null=True, verbose_name=b'Bug\xe5\x86\x85\xe5\xae\xb9')),
                ('img', models.ImageField(default=b'', upload_to=b'', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
                ('result', models.BooleanField(default=False, verbose_name=b'\xe5\xa4\x84\xe7\x90\x86\xe6\x83\x85\xe5\x86\xb5')),
            ],
        ),
    ]
