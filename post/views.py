from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from yaml import load
from .models import Postagem
from .models import Curso
from empresa.models import Empresa
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User

@login_required
def publicacoes(request):
    postagens = Postagem.objects.all().order_by('-created_at').filter(user = request.user)
    #perfil = User.objects.all()
    return render(request,'post/listar.html',{'postagens': postagens,})


@login_required
def criar(request):

    if request.method == "POST":
        form = PostForm(request.POST) 
        if form.is_valid():
            #user = request.user
            post = form.save(commit=False)
            post.user = request.user
            form.save()
                #user = request.user
                #post = form.save(commit=False)
                #post.customer=request.user    #:(
                #user = Postagem.objects.create(user=user)
            return HttpResponseRedirect("/post")

    else:
         form = PostForm()
    
    
    return render(request, 'post/criar.html', {'form': form})

@login_required
def excluir(request, postagem_id):
       
    Postagem.objects.get(pk=postagem_id).delete()
    
    return HttpResponseRedirect("/post")

@login_required
def editar(request, postagem_id):

    postagem= Postagem.objects.get(pk=postagem_id)
    
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=postagem)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/post")
    else:
        form = PostForm(instance=postagem)
    context = {
        'form': form,
        'postagem_id': postagem_id
    }
    
    return render(request, 'post/editar.html', context)

@login_required
def feed(request, curso):

    for postagens in curso:
        if curso == curso:
            postagens = Postagem.objects.filter(curso=curso).values('titulo', 'descricao', 'curso')
            curso = Curso.objects.filter(id = curso).values('nome')
            #a = Postagem.get_cursos_display()
            return render(request, 'post/feed.html', {'postagens': postagens, 'curso':curso}) 
 
    return render(request, 'post/editar.html', {'postagens': postagens})  


