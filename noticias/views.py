import sys
sys.path.append("C:\\Users\\felip\\Desktop\\mini-blog")

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'person.settings')
import django
django.setup()
from logging import Logger


from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from usuarios.models import UserProfile

from noticias.models import Noticias

# Create your views here.


@login_required
def cadastrar_noticias(request):
    user = User.objects.get(username = request.user.username)
    if request.method == 'GET':
        return render(request, 'noticias/nova_noticia.html',context={'user':user})

    elif request.method == 'POST':
        
        notice = request.POST.get('mensagem')
        titulo = "isso aqui deve ser temporario, apagar em breve"
        user = User.objects.get(id=request.user.id)
        if len(titulo) == 0:
            noticias = Noticias.objects.create(
                user=user,
                titulo='Sem titulo cadastrado',
                notice=notice
            )
        else:
            noticias = Noticias.objects.create(
                user=user,
                titulo=titulo,
                notice=notice
            )

        return redirect('mural')


def noticias(request):
    noticias = Noticias.objects.all().order_by('-numero')


 

    if request.user.is_authenticated:
  
        user = request.user
        
    
        pessoa = UserProfile.objects.get(user=request.user)

        return render(request, 'noticias/mural_novo.html',
                      context={'noticias': noticias,
                               'user': user, 'pessoa': pessoa,})

    else:
    
        return render(request, 'noticias/mural_novo.html',
                      context={'noticias': noticias})


@ login_required
def aviso_deletar(request, id):
    try:
        aviso_del = Noticias.objects.get(id=id)
    except:
        return redirect('not_found')

    if request.user == aviso_del.user:
        if request.method == 'POST':
            aviso_del.delete()
            return redirect('mural')
    else:
        return redirect('not_found')
    return render(request, 'noticias/aviso_deletar.html', context={'aviso_del': aviso_del})


@ login_required
def noticia_nova(request, id):
    
    noticia = Noticias.objects.get(id=id)
    
    if request.user == noticia.user:
        if request.method == 'POST':
            notice = request.POST.get('mensagem')

        # Atualize os campos da notícia
            noticia.notice = notice
            noticia.atualizado = True
            noticia.save()
        # utilizar um boleano, caso a noticia seja atualizada
        # Redirecione para a página de notícias após a atualização
            return redirect('mural')
    else:
        return redirect('not_found')

    return render(request, 'noticias/nova_noticia_nova.html', {'noticia': noticia})


@login_required
def perfil(request):
    pessoa = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        texto = request.POST.get('texto-perfil')
        imagem = request.FILES.get('imagem')

        user_profile, created = UserProfile.objects.get_or_create(
            user=request.user)

        if texto:
            user_profile.profile_text = texto

        if imagem:  # Verifica se uma imagem foi enviada
            user_profile.profile_image = imagem

        user_profile.save()

        return redirect('mural')

    return render(request, 'noticias/editar-perfil.html', context={'pessoa': pessoa})
@login_required
def mensagens_publicadas(request,id):
    noticias = Noticias.objects.filter(user_id = id)
    pessoa = noticias.first()
    return render(request,'noticias/mensagens_usuario.html',context={'noticias':noticias,'pessoa':pessoa})

@login_required
def visualizar(request,id):
    noticia = Noticias.objects.get(id=id)
    return render(request, 'noticias/mensagem_completa.html', context={'noticia':noticia})

def outperfil(request, id):
    perfil = UserProfile.objects.get(id=id)
    return render(request, 'noticias/perfil_fora.html',
                  context={'perfil': perfil})
@login_required
def curtida(request, id):
    noticias = Noticias.objects.get(id=id)
    

    if request.user in noticias.curtida.all():
            
        noticias.curtida.remove(request.user)
        
    
    
    else:
        noticias.curtida.add(request.user)
        

    noticias.numero += noticias.aqui()
    noticias.save()
    
    return redirect('mural')
        

def necessita_login(request):
    return render(request,'noticias/necessita_login.html')
   