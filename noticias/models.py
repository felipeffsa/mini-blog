from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.db import models




# Create your models here.
class Noticias(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'noticias_autor')
    titulo = models.CharField(max_length=50)
    notice = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    atualizado = models.BooleanField(default=False)
    curtida = models.ManyToManyField(User)
    
   
    def __str__(self) -> str:
        return self.titulo

  