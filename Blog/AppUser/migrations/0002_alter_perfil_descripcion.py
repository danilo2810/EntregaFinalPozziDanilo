# Generated by Django 4.1.3 on 2023-01-08 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='descripcion',
            field=models.TextField(max_length=300),
        ),
    ]
