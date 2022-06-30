
from django.db import models

class Discente(models.Model):
    
    nome = models.CharField('Nome', max_length = 50, null = True)
    usuario = models.CharField('Usuário', max_length = 20, null = True)
    email = models.EmailField('E-mail',max_length = 50, null = True)
    serie = models.CharField('Série', max_length = 10, null = True)
    turma = models.CharField('Turma', max_length = 10, null = True)
    cidade = models.CharField('Cidade', max_length = 50, null = True)
    telefone = models.CharField('Telefone',max_length = 20, null = True)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True, null = True)

    
    def __str__(self):
        return (self.nome)
    def __str__(self):
        return (self.serie)
    def __str__(self):
        return (self.cidade)
    def __str__(self):
        return (self.telefone)
    def __str__(self):
        return (self.turma)
    def __str__(self):
        return (self.cidade)
