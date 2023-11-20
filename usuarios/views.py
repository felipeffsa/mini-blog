from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.shortcuts import redirect, render

PROHIBITED_WORDS = ['hitler', 'merda', 'vadia',
                    'Hitler', 'Nazismo', 'nazi', 'Nazi', 'nazismo',]
PALAVRAS = ['@', '$', '%', '!', '#', '&', '*']
NUMEROS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def cadastro(request):
    cadastrado = User.objects.all()
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        nome = request.POST['nome']
        senha = request.POST['senha']
        repetir_senha = request.POST['repetir_senha']

    for word in PROHIBITED_WORDS:
        if nome == word:
            messages.add_message(request, constants.ERROR,
                                 'Você não pode utilizar esse tipo de nome como nickname')
            return render(request, 'cadastro.html')

    if len(nome) > 10:
        messages.add_message(request, constants.WARNING,
                             ' O usuario esta com mais de 10 caracteres')
        return redirect('cadastro')
    if len(senha) < 6:
        nome = {'nome': nome}
        messages.add_message(request, constants.ERROR,
                             'A senha está com menos de 6 caracteres')
        return render(request, 'cadastro.html', context={'nome': nome})
    if senha != repetir_senha:
        messages.add_message(request, constants.ERROR,
                             'As senhas não são iguais')
        return render(request, 'cadastro.html', context={'nome': nome})

    for cadastro in cadastrado:
        if nome == cadastro.username:
            messages.add_message(request, constants.ERROR,
                                 'O usuário já esta cadastrado no sistema, porfavor utilize outro nome de usuario')
            return render(request, 'cadastro.html')

    user = User.objects.create_user(
        username=nome,
        password=senha
    )
    messages.add_message(request, constants.SUCCESS,
                         'Usuário cadastrado com sucesso')
    return render(request, 'cadastro.html')


def logar(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        senha = request.POST['senha']
        nome = request.POST['nome']
        # aqui verifica se o usuario pertence ao banco de dados,
        #  caso contrário irá retornar um NONE
        user = authenticate(username=nome, password=senha)
        if user:
            login(request, user)
            return redirect('mural')
        else:
            return redirect('not_found')


def sucesso(request):
    return render(request, 'sucesso.html')


def not_found(request):
    return render(request, 'not_found.html')


def sair(request):
    logout(request)
    return redirect('login')
