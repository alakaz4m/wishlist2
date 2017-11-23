# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 07:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('LoginReg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_added', to='LoginReg.User')),
                ('wished_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_wished', to='LoginReg.User')),
            ],
        ),
    ]
