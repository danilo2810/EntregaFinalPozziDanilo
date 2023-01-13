from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', inicio ,name='inicio'),
    path('aboutMe', aboutMe ,name='aboutMe'),
    path('registro/', registro,name='registro'),
    path('login/', login_usuario,name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('mensajeria/', mensajeria ,name='mensajeria'),
    path('verperfil/', verperfil ,name='verperfil'),
    path('editarperfil/', editarperfil ,name='editarperfil'),
    path('eliminarperfil/', eliminarperfil ,name='eliminarperfil'),
    path('leermensaje/<id>', leermensaje ,name='leermensaje'),
    path('vermensaje/<id>', vermensaje ,name='vermensaje'),
    path('responderMensaje/<id>', responderMensaje ,name='responderMensaje'),
  
]