# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]