from django.db import models
from django.utils import timezone

class Grupo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class ContaPagar(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='contas')
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()
    pago = models.BooleanField(default=False)
    data_pagamento = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.descricao} - {self.grupo.nome}"
    
    class Meta:
        ordering = ['data_vencimento']
