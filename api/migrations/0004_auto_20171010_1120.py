# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_playerlist_palyer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerlist',
            name='palyer_type',
            field=models.CharField(choices=[('BATING', 'Bating'), ('BOWLER', 'Bowler'), ('ALLROUNDER', 'All Rounder'), ('KEEPER', 'Keeper')], default='Bowler', max_length=10),
        ),
    ]