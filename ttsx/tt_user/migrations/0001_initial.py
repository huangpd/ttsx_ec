# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('uname', models.CharField(max_length=10)),
                ('upwd', models.CharField(max_length=40)),
                ('uaddr', models.CharField(max_length=100, default='')),
                ('uphone', models.CharField(max_length=11, default='')),
                ('umail', models.CharField(max_length=20)),
                ('ucode', models.CharField(max_length=6, default='')),
                ('ushou', models.CharField(max_length=10, default='')),
            ],
        ),
    ]
