from django.urls import path

from . import views

urlpatterns = [
    path('criar/', views.criar, name='criar'),
    path('perfil/<int:empresa_id>/', views.perfil, name = 'perfil' ),
    path('editar/<int:empresa_id>/', views.editar, name = 'editar')
]