# Generated by Django 4.1.1 on 2022-11-21 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_boleta_anio_doc_boleta_dia_doc_boleta_folio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='boleta',
            name='comentario',
            field=models.CharField(default=100, max_length=100),
            preserve_default=False,
        ),
    ]
