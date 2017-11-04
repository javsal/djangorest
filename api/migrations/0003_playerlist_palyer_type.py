# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20171010_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerlist',
            name='palyer_type',
            field=models.CharField(choices=[('BATING', 'Bating'), ('BOWLER', 'Bowler'), ('ALLROUNDER', 'All Rounder'), ('KEEPER', 'Keeper')], default='ALLROUNDER', max_length=10),
        ),
    ]