# Generated by Django 4.1.3 on 2023-01-08 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUser', '0004_alter_perfil_sitio_web'),
    ]

    operations = [
        migrations.CreateModel(
            name='mensajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emisor', models.CharField(max_length=30)),
                ('receptor', models.CharField(max_length=30)),
                ('cuerpo_mensaje', models.TextField(max_length=200)),
                ('estado', models.BooleanField()),
            ],
        ),
    ]
