# Generated by Django 4.1.7 on 2023-05-30 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basedata', '0002_formularios_saq'),
    ]

    operations = [
        migrations.AddField(
            model_name='formularios_saq',
            name='tipo_cliente',
            field=models.CharField(default='', max_length=16),
        ),
    ]
