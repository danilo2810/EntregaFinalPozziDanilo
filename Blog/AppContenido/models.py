from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Post(models.Model):
    titulo=models.CharField(max_length=50)
    subtitulo=models.CharField(max_length=100)
    cuerpo = RichTextField()
    autor=models.CharField(max_length=50)
    fechaCreacion=models.DateTimeField()
    fechaModificacion=models.DateTimeField()
    imagen=models.ImageField(upload_to='posteos')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f'({self.user.username},{self.titulo})'
