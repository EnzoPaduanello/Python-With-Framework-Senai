# Generated by Django 5.1 on 2024-08-24 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0005_alter_estacionamento_hrentrada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamento',
            name='hrEntrada',
            field=models.TimeField(auto_now_add=True, verbose_name='Horário de Entrada'),
        ),
    ]
