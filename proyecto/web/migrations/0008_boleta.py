# Generated by Django 4.1.1 on 2022-11-01 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_delete_boleta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut_emisor', models.CharField(max_length=30)),
                ('rut_receptor', models.CharField(max_length=30)),
                ('tipo_servicio', models.CharField(max_length=30)),
            ],
        ),
    ]
