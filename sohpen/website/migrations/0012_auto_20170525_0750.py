# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='membership_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
