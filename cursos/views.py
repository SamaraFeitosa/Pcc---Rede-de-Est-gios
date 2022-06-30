from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Curso
from .forms import CursosForm
from django.http import HttpResponseRedirect


@login_required
def home(request):
    curso = Curso.objects.all().order_by('-created_at')
    return render(request,'cursos/home.html', {'curso': curso})

@login_required
def cadastro(request):
  
    if request.method == "POST":
        form = CursosForm(request.POST)
    
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/cursos")

    else:
        form = CursosForm()
    
    return render(request, 'cursos/cadastro_cursos.html', {'form': form})


@login_required
def excluir(request, curso_id):
       
    Curso.objects.get(pk=curso_id).delete()
    
    return HttpResponseRedirect("/cursos")

@login_required
def editar(request, curso_id):

    curso= Curso.objects.get(pk=curso_id)
    
    if request.method == "POST":
        form = CursosForm(request.POST, instance=curso)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/cursos")
    else:
        form = CursosForm(instance=curso)
    context = {
        'form': form,
        'curso_id': curso_id
    }
    return render(request, 'cursos/editar.html', context)