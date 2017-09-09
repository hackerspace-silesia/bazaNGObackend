# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 04:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_auto_20170909_0436'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nazwa')),
            ],
        ),
        migrations.AlterField(
            model_name='organization',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='organization|is_active'),
        ),
        migrations.AddField(
            model_name='category',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Organization'),
        ),
    ]
