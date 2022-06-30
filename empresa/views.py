from django.http import HttpResponseRedirect
from django.shortcuts import render

from empresa.forms import EmpresaForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from .models import Empresa

# Create your views here.
def criar(request):

    if request.method == "POST":
        form = EmpresaForm(request.POST)
            
        if form.is_valid():
            new_user = form.save()
            g_empresa = Group.objects.get(name='empresa')
            new_user.groups.add(g_empresa)
            new_user.save()
            
        return HttpResponseRedirect('/accounts/login/')
            
    else:
        form = EmpresaForm()
        
    context = {
        'form': form
    }
        
    return render(request, 'empresa/criar.html', context)

@login_required
def perfil(request, empresa_id):
    empresa = Empresa.objects.get(pk=empresa_id)
    return render(request,'empresa/perfil.html',{'empresa': empresa})

@login_required
def editar(request, empresa_id):
    empresa= Empresa.objects.get(pk=empresa_id)
    
    if request.method == "POST":
        form = EmpresaForm(request.POST, instance=empresa)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/post")
    else:
        form = EmpresaForm(instance=empresa)
    context = {
        'form': form,
        'empresa_id': empresa_id
    }
    
    return render(request, 'empresa/editar.html', context)