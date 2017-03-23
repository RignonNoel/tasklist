# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-23 03:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20170323_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_by',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='task_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
            preserve_default=False,
        ),
    ]
