from django import views
from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name="home"),
    path('cadastro/', views.cadastro, name = 'cadastro'),
     path('excluir/<int:curso_id>/',views.excluir,  name='excluir'),
    path('editar/<int:curso_id>/', views.editar, name = 'editar'),
]