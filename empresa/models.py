from django.db import models
from django.contrib.auth.models import User


class Empresa(User):
    nome = models.CharField('Nome Social da Empresa', max_length=50, null=True)
    cnpj = models.CharField('CNPJ', max_length=10, null=True)
    contato = models.CharField('Contato', max_length=11, null=True)
    rua = models.CharField('Rua', max_length=60, null=True)
    numero = models.CharField('Numero do Prédio', max_length=4, null=True)
    bairro = models.CharField('Bairro', max_length=120, null=True)
    cep = models.CharField('CEP', max_length=8, null=True)
    razaosocial = models.CharField('Razão Social', max_length=50, null=True)

    def __str__(self):
        return self.nome