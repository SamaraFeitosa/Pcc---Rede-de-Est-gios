
from django.db import models
from django.contrib.auth.models import User
from cursos.models import Curso

escolaridade= (
         ("Ensino médio Integrado ao Técnico", "Ensino médio Integrado ao Técnico"),
         ("Técnologo", "Técnologo"),
         ("Licenciatura","Licenciatura"),
         ("Bacharelado", "Bacharelado"),
         ("Pós-Graduaçao", "Pós-Graduação") )

remunerado = (("Sim", "Sim"),
              ("Não", "Não"))
class Postagem(models.Model):
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE, null = True)
    user= models.ForeignKey(User, on_delete=models.CASCADE, null = True, verbose_name = "Usuário")
    titulo = models.CharField(max_length = 100, verbose_name = "Titulo")
    descricao= models.TextField(verbose_name = "Descrição")
    imagem = models.ImageField(blank=True, null=True, verbose_name = "Imagem")
    escolaridade = models.CharField(max_length=70,choices=escolaridade,verbose_name = "Escolaridade requerida")
    remuneracao = models.CharField(max_length= 10, choices=remunerado, verbose_name = "Remunerado")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.titulo)
    def __str__(self):
        return str(self.user)
    def __str__(self):
        return str(self.descricao)
    def __str__(self):
        return str(self.imagem)
    def __str__(self):
        return str(self.escolaridade)
    def __str__(self):
        return str(self.remuneracao)
    def __str__(self):
        return str(self.created_at)
    def __srt__(self):
        return str(self.updated_at)

  


    