# Generated by Django 5.1 on 2024-08-24 17:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_rename_dtentrada_estacionamento_hrentrada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamento',
            name='hrEntrada',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
