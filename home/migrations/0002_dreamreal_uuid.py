# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-25 11:51
from __future__ import unicode_literals

from django.db import migrations
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dreamreal',
            name='uuid',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, unique=True),
        ),
    ]