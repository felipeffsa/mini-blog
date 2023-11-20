from django.urls import path

from usuarios import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.logar, name='login'),
    path('not_found/', views.not_found, name='not_found'),
    path('sucesso/', views.sucesso, name='sucesso'),
    path('sair/', views.sair, name='sair')
]
