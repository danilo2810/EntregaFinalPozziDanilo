# Generated by Django 4.1.3 on 2023-01-08 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUser', '0003_alter_perfil_sitio_web'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='sitio_web',
            field=models.TextField(max_length=40),
        ),
    ]
