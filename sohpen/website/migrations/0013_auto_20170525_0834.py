# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20170525_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='description_of_work_1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='member',
            name='description_of_work_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='description_of_work_3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='description_of_work_4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='description_of_work_5',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
