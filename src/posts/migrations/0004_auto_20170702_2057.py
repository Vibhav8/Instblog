# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 20:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 7, 2, 20, 57, 10, 535389, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
