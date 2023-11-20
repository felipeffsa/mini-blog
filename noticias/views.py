from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from usuarios.models import UserProfile

from .models import Noticias

# Create your views here.


@login_required
def cadastrar_noticias(request):
    if request.method == 'GET':
        return render(request, 'noticias/cadastro_noticias.html')

    elif request.method == 'POST':
        titulo = request.POST['titulo']
        notice = request.POST['notice']
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

        return render(request, 'noticias/cadastro_noticias.html')


def noticias(request):
    noticias = Noticias.objects.all().order_by('-id')

    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        pessoa = UserProfile.objects.get(user=request.user)

        return render(request, 'noticias/mural.html',
                      context={'noticias': noticias,
                               'user': user, 'pessoa': pessoa})

    else:

        return render(request, 'noticias/mural.html',
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
    try:
        noticia = Noticias.objects.get(id=id)
    except:
        return redirect('not_found')
    if request.user == noticia.user:
        if request.method == 'POST':
            titulo = request.POST['titulo']
            notice = request.POST['notice']

        # Atualize os campos da notícia
            noticia.titulo = titulo
            noticia.notice = notice
            noticia.atualizado = True
            noticia.save()
        # utilizar um boleano, caso a noticia seja atualizada
        # Redirecione para a página de notícias após a atualização
            return redirect('mural')
    else:
        return redirect('not_found')

    return render(request, 'noticias/noticia_nova.html', {'noticia': noticia})


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

    return render(request, 'noticias/perfil.html', context={'pessoa': pessoa})


def outperfil(request, id):
    perfil = UserProfile.objects.get(id=id)
    return render(request, 'noticias/outperfil.html',
                  context={'perfil': perfil})
