from django import views
from django.urls import path
from .import views
urlpatterns = [
    path('', views.listar, name="listar"),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('excluir/<int:discente_id>/',views.excluir,  name='excluir'),
    path('editar/<int:discente_id>/', views.editar, name = 'editar'),
    path('perfil/<int:discente_id>/', views.perfil, name = 'perfil'),
    path('home/', views.home, name="home"),
]