# Generated by Django 5.0 on 2024-01-22 14:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0023_remove_noticias_curtida_alter_noticias_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='curtida',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
