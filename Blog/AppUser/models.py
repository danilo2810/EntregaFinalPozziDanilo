from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    
    descripcion=models.TextField(max_length=300)
    sitio_web=models.TextField(max_length=40)
    imagen=models.ImageField(upload_to='avatars',blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f'({self.user.username})'

class Mensajes(models.Model):
    emisor=models.CharField(max_length=30)
    receptor=models.CharField(max_length=30)
    cuerpo_mensaje=models.TextField(max_length=200)
    leido=models.BooleanField()
    def __str__(self):
        return f'(Emisor: {self.emisor} Receptor: {self.receptor} Leido: {self.leido})'


