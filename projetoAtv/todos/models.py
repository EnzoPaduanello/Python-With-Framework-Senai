from django.db import models
from django.utils import timezone

# Create your models here.


class Estacionamento(models.Model):
    nomeCliente = models.CharField(verbose_name="Nome do Cliente", max_length=150, null=False, blank=False)
    placaVeiculo = models.CharField(verbose_name="Placa do Veículo", max_length=7, null=False, blank=False)
    tipoVeiculo = models.CharField(verbose_name="Tipo do Veículo", max_length=150, null=False, blank=False)
    hrEntrada = models.TimeField(default=timezone.now, null=False, blank=False)
    hrSaida = models.TimeField(verbose_name="Data de Saída", null=True, blank=True)