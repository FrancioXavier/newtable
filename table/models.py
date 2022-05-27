from django.db import models

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=25)
    farinha_ou_insumo = models.CharField(max_length=25)
    preco = models.FloatField()
    data = models.DateField()

    def __str__(self):
        return self.nome
