# Generated by Django 4.1.7 on 2023-05-12 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_alter_clientes_telefono2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificados',
            name='codigo_certificado',
            field=models.CharField(max_length=20),
        ),
    ]
