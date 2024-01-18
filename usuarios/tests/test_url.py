from django.test import TestCase
from django.urls import reverse
# Create your tests here.
class BlogUrlTest(TestCase):
    def test_url_do_blog_pessoal(self):
        assert 1==1
    def test_testinho_blog_pessoal(self):
        assert 2==2
    def test_url_aqui_blog_pessoal(self):
        url = reverse('cadastro')
        self.assertEqual(url,'/cadastro/')
