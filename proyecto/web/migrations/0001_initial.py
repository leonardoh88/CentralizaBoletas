# Generated by Django 4.1.1 on 2022-09-09 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35)),
                ('rut', models.CharField(max_length=20)),
                ('contraseña', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=70)),
                ('comentario', models.CharField(max_length=100)),
            ],
        ),
    ]
