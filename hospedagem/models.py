from django.db import models


class Consumo(models.Model):
    apartamento = models.IntegerField()
    valor = models.FloatField()

    def __str__(self):
        return str(self.apartamento)


class Quarto(models.Model):
    numero = models.IntegerField()
    data = models.DateField()
    valor = models.FloatField()

    def __str__(self):
        return str(self.numero)


class Hospedagem(models.Model):
    data_entrada = models.DateField()
    data_saida = models.DateField()
    valor = models.FloatField()
    consumo = models.ForeignKey(Consumo, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.data_entrada)


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    hospedagem = models.ForeignKey(Hospedagem, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
