# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-10 22:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('education', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='people',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.People'),
        ),
    ]
