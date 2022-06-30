from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cursos.models import Curso
from .models import Discente
from .forms import DiscenteForm
from django.http import HttpResponseRedirect


@login_required
def listar(request):
    discente = Discente.objects.all().order_by('-created_at')
    return render(request,'discente/listar.html', {'discente': discente})

@login_required
def perfil(request, discente_id):
    discente = Discente.objects.get(pk=discente_id)
    return render(request,'discente/perfil.html',{'discente': discente})

@login_required
def home(request):
    curso = Curso.objects.all().order_by('-created_at')
    return render(request,'discente/home.html', {'curso': curso})

@login_required
def cadastro(request):
  
    if request.method == "POST":
        form = DiscenteForm(request.POST)
    
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/discente")

    else:
        form = DiscenteForm()
    
    return render(request, 'discente/cadastro_discente.html', {'form': form})


@login_required
def excluir(request, discente_id):
       
    Discente.objects.get(pk=discente_id).delete()
    
    return HttpResponseRedirect("/discente")

@login_required
def editar(request, discente_id):

    discente= Discente.objects.get(pk=discente_id)
    
    if request.method == "POST":
        form = DiscenteForm(request.POST, instance=discente)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/discente")
    else:
        form = DiscenteForm(instance=discente)
    context = {
        'form': form,
        'discente_id': discente_id
    }
    return render(request, 'discente/editar.html', context)