from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.db import models




# Create your models here.
class Noticias(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='noticia')
    titulo = models.CharField(max_length=50)
    notice = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    atualizado = models.BooleanField(default=False)
    curtida = models.ManyToManyField(User, related_name='noticas_curtida')
    numero = models.IntegerField(default=0)
    
    
    def aqui(self):
        curtidas = [resultado for resultado in self.curtida.all()]
        return len(curtidas)
    
   
    def __str__(self) -> str:
        return self.titulo

  