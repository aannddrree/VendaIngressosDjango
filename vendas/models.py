from django.db import models


class Torcedor(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=70)
    idade = models.PositiveSmallIntegerField()

    def __str__(self):
        return "CPF: " + self.cpf + " - Nome: " + self.nome + " - Idade: " + str(self.idade)


class Ingresso(models.Model):
    preco = models.PositiveIntegerField()
    setor = models.CharField(max_length=30)
    clubeA = models.CharField(max_length=30)
    clubeB = models.CharField(max_length=30)
    estadio = models.CharField(max_length=40)
    status = models.CharField(max_length=40, default='Disponível')

    def __str__(self):
        return "R$" + str(self.preco) + " - Setor: " + self.setor + " - " + self.clubeA\
               + " X " + self.clubeB + " - Estádio: " + self.estadio


class Compra(models.Model):
    torcedor = models.ForeignKey(Torcedor, on_delete=models.SET_NULL, null=True)
    ingresso = models.ForeignKey(Ingresso, on_delete=models.SET_NULL, null=True)
