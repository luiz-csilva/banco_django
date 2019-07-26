from django.db import models

class Pessoa(models.Model):
    GENEROS = (('M','Masculino'),('F','Feminino'),('O','Outros'))
    nome = models.CharField(max_length=255, default='unknow')
    cpf = models.CharField(max_length=14)
    email = models.EmailField(max_length = 255)
    telefone = models.CharField(max_length = 255)
    genero = models.CharField(max_length=255, choices=GENEROS)

    def __str__(self):
        return self.nome

class Conta(models.Model):
    pessoa = models.ForeignKey(
        Pessoa, on_delete = models.CASCADE
    )
    numero_conta = models.CharField(max_length=255)
    saldo = models.FloatField(default=0.0)
    agencia = models.CharField(max_length=255)
    nome_banco = models.CharField(max_length=255, default='mybank', null=True)