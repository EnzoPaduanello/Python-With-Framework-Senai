from django.db import models

# Create your models here.

class Estacionamento(models.Model):
    nomeCliente = models.CharField(max_length=150, null=False, blank=False)
    placaVeiculo = models.CharField(max_length=7, null=False, blank=False)
    tipoVeiculo = models.CharField(max_length=150, null=False, blank=False)
    dtEntrada = models.DateField(auto_now_add=True, null=False, blank=False)
    dtSaida = models.DateField(null=True)