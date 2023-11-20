from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        upload_to='imagens/', blank=True, null=True)
    profile_text = models.TextField(blank=True)

    def add_default_image(user_profile):
        default_image_path = 'img/castor.png'
        user_profile.profile_image = default_image_path
        user_profile.save()

# Usando um sinal para criar um perfil quando um novo usuário é criado


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        new_profile = UserProfile.objects.create(user=instance)
        UserProfile.add_default_image(new_profile)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
