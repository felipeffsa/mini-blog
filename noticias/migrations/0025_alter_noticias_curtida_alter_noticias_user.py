# Generated by Django 5.0 on 2024-02-06 01:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0024_alter_noticias_curtida'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='curtida',
            field=models.ManyToManyField(related_name='noticas_curtida', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
