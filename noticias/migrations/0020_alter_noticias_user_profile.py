# Generated by Django 4.2.6 on 2023-10-28 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_userprofile_delete_usuario'),
        ('noticias', '0019_noticias_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.userprofile'),
        ),
    ]
