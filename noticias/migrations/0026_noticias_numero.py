# Generated by Django 5.0 on 2024-02-06 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0025_alter_noticias_curtida_alter_noticias_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticias',
            name='numero',
            field=models.IntegerField(default=0),
        ),
    ]
