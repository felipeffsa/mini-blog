from django.urls import reverse,resolve
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from noticias.models import Noticias
from usuarios.views import cadastro
class TestUrlDinamica(TestCase):
    def test_url_create_register(self):
        url = reverse('cadastro')
        response = self.client.get(url).content.decode('utf-8')
        url_resolve = resolve(reverse('cadastro'))
        self.assertIn('Usuario:',response)
        self.assertIn('Entrar',response)
        self.assertEqual(url_resolve.func,cadastro)
    
    def test_url_login(self):
        url = reverse('login')
        response = self.client.get(url).content.decode('utf-8')
     
        self.assertIn('Não possui uma conta ?',response)
        self.assertIn('Login',response)
        
    
    def test_login_fail(self):
        # Teste de autenticação mal-sucedido
        user = authenticate(username='felipe', password='senha_errada')
        self.assertIsNone(user)
      

    def setUp(self):
        # Crie um usuário para testar a autenticação
        self.usuario = User.objects.create_user(
            username='felipe',
            password='tom10112425'
        )

        # Crie uma notícia associada ao usuário
        self.noticia = Noticias.objects.create(
            user=self.usuario,
            titulo='Pequeno Teste',
            notice='Algo a ser feito',
            data=True,
            atualizado=False,
            curtida=1
        )

        # Login do usuário
        self.client.login(username='felipe', password='tom10112425')

    def test_mensagem(self):
        # Obter a URL para visualizar a notícia
        url = reverse('visualizar', kwargs={'id': self.noticia.id})

        # Fazer uma solicitação GET para a URL
        response = self.client.get(url)

        # Verificar se a resposta foi bem-sucedida (status_code 200)
        self.assertEqual(response.status_code, 200)

        # Verificar se o título da notícia na resposta é o esperado
        self.assertEqual(response.context['visualizar'].notice, 'Algo a ser feito')
        ...
      
    
    def test_deletar_mensagem(self):
        url = reverse('aviso_deletar',kwargs={'id':self.noticia.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        deletar = Noticias.objects.get(id = self.noticia.id)
        deletar.delete()