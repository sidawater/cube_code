# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-08 13:41
from __future__ import unicode_literals

from django.db import migrations
from fixture.data_getter import get_initial_dat


def initial_coding_map(apps, schema_editor):
    MemoryMapKey = apps.get_model('codemap', 'MemoryMapKey')
    SignificantValue = apps.get_model('codemap', 'SignificantValue')

    data_map = get_initial_dat()
    for key in data_map.keys():
        memory_map_key = MemoryMapKey.objects.create(name=key)
        memory_map_key.save()
        for value in data_map[key]:
            sign_value = SignificantValue.objects.create(
                key=memory_map_key,
                content=value,
                remark=''
            )
            sign_value.save()



class Migration(migrations.Migration):

    dependencies = [
        ('codemap', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_coding_map),
    ]
