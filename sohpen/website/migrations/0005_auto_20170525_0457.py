# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 04:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20170518_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='url',
            field=models.CharField(help_text='/pages/1/', max_length=50),
        ),
    ]
