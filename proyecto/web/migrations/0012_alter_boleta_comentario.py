# Generated by Django 4.1.1 on 2022-11-21 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_boleta_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta',
            name='comentario',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
