# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-30 06:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=10000, verbose_name='评论')),
                ('link', models.CharField(max_length=10000, verbose_name='链接')),
                ('status', models.IntegerField(choices=[(0, '正常'), (-1, '删除')], default=0, verbose_name='状态')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name_plural': '消息',
                'verbose_name': '消息',
            },
        ),
    ]