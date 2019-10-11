# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-11 10:41
from __future__ import unicode_literals

from django.db import migrations, models
import final.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200, verbose_name=final.models.Image)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('image_name', models.CharField(max_length=200)),
                ('image_description', models.TextField(max_length=600)),
                ('image_link', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200, verbose_name=final.models.Image)),
            ],
        ),
    ]