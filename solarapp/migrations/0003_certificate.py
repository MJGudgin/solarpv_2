# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-20 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solarapp', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_number', models.IntegerField()),
                ('cid', models.IntegerField()),
                ('userID', models.IntegerField()),
                ('report_number', models.IntegerField()),
                ('issue_date', models.DateField()),
                ('standard_id', models.IntegerField()),
                ('location_id', models.IntegerField()),
                ('model_number', models.IntegerField()),
            ],
        ),
    ]
