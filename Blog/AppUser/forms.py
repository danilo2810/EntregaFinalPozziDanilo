from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    username=forms.CharField(label='Usuario')
    email=forms.EmailField(label='Email')
    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirmar contraseña',widget=forms.PasswordInput)
    class Meta():
        model=User
        fields=['username','email','password1','password2']
        help_texts={k:'' for k in fields}

class EditarUserForm(UserCreationForm):
    first_name=forms.CharField(label='Nombre',widget=forms.Textarea(attrs={"rows":"1",'cols':'19'}))
    last_name=forms.CharField(label='Apellido',widget=forms.Textarea(attrs={"rows":"1",'cols':'19'}))
    email=forms.EmailField(label='Email',widget=forms.Textarea(attrs={"rows":"1",'cols':'19'}))
    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirmar contraseña',widget=forms.PasswordInput)
    class Meta():
        model=User
        fields=['email','password1','password2','first_name','last_name']
        help_texts={k:'' for k in fields}

class EditarPerfilForm (forms.Form):
    descripcion=forms.CharField(label='Descripcion personal',required=False,widget=forms.Textarea(attrs={"rows":"5",'cols':'19'}))
    sitio_web=forms.CharField(label='Sitio web',widget=forms.Textarea(attrs={"rows":"1",'cols':'19'}))
    imagen=forms.ImageField(label='Imagen')

class MensajeriaForm(forms.Form):
    receptor=forms.CharField(max_length=30,widget=forms.Textarea(attrs={"rows":"1",'cols':'50'}))
    cuerpo_mensaje=forms.CharField(max_length=200,widget=forms.Textarea(attrs={"rows":"10",'cols':'50'}))
    
