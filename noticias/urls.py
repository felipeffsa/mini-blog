from django.urls import path

from noticias import views

urlpatterns = [
    path('cadastrar-noticias/', views.cadastrar_noticias,
         name='cadastrar-noticias'),
    path('mural/', views.noticias, name='mural'),
    path('aviso_deletar/<int:id>/', views.aviso_deletar, name='aviso_deletar'),
    path('noticia_nova/<int:id>/', views.noticia_nova, name='noticia_nova'),
    path('perfil/', views.perfil, name='perfil'),
    path('outperfil/<int:id>/', views.outperfil, name='out_perfil')


]
