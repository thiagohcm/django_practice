from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome do cliente')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Telefone(models.Model):
    telefone = models.PositiveIntegerField(verbose_name='Telefone')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')

    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'
