from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from usuarios.forms import CadastroUser,AuthenticationForm, CustomLogin
from django.contrib.messages import constants
from django.shortcuts import redirect, render



def cadastro(request):
    if request.method == "POST":
        form = CadastroUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return redirect('cadastro')
    else:
        form = CadastroUser()
        return render(request,'cadastro_novo.html',context={'form':form})

def logar(request):

    if request.method =='POST':
        form = CustomLogin(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('mural')
            else:
                messages.add_message(request, constants.ERROR,'Usuário ou senha inválido')
                return redirect('login')
        else:
            messages.add_message(request, constants.ERROR,'Usuário ou senha inválido')
            return render(request, 'login_novo.html', context={'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'login_novo.html', context={'form': form})


def sucesso(request):
    return render(request, 'sucesso.html')


def not_found(request):
    return render(request, 'error_404.html')


def sair(request):
    logout(request)
    return redirect('login')
