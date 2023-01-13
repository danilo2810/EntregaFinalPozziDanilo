from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from AppUser.views import *



urlpatterns = [
    path('nuevoPost/', nuevoPost ,name='nuevoPost'),
    path('leerPost/<id>', leerPost ,name='leerPost'),
    path('editarPost/<id>', editarPost ,name='editarPost'),
    path('eliminarPost/<id>', eliminarPost ,name='eliminarPost'),
    path('todosPost', todosPost ,name='todosPost'),
    path('buscarPostTitulo', buscarPostTitulo ,name='buscarPostTitulo'),

]