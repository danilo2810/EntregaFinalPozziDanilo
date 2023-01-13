from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget



class crearPost(forms.Form):
    titulo=forms.CharField(label='Titulo del post',widget=forms.Textarea(attrs={"rows":"1",'cols':'25'}))
    subtitulo=forms.CharField(label='Subtitulo del post')
    cuerpo = forms.CharField(label='Contenido del post',widget = CKEditorWidget())
    imagen=forms.ImageField(label='Imagen')