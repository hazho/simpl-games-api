# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 20:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpl', '0003_auto_20160325_2052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phase',
            old_name='position',
            new_name='order',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='rounds_count',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='world',
        ),
    ]