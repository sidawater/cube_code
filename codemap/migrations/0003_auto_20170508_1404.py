# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-08 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codemap', '0002_auto_20170508_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='significantvalue',
            name='related_type',
            field=models.CharField(choices=[('acronym', '拼写缩写'), ('comics', '动漫'), ('game', '游戏'), ('Internet', '网络用语'), ('dialect', '方言俗语'), ('personal', '个人专用'), ('others', '其他')], default='acronym', max_length=30, verbose_name='联想类型'),
        ),
        migrations.AlterField(
            model_name='significantvalue',
            name='remark',
            field=models.CharField(default='', max_length=512, verbose_name='描述'),
        ),
    ]
