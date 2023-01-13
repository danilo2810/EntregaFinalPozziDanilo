from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from AppContenido.models import *

def obtener_avatar(request):
    lista=Perfil.objects.filter(user=request.user)
    if len(lista)!=0:
        url_avatar=lista[0].imagen.url
    else:
        url_avatar='/media/avatars/avatar_defecto.jpg'
    return url_avatar

def buscarmensaje(request):
    nuevos_mensajes=[]
    mensajesAntiguos=[]
    usuario=request.user
    mensajes=Mensajes.objects.filter(receptor=usuario)
    mensajesEnviados=Mensajes.objects.filter(emisor=usuario)
    for item in mensajes:
        if not item.leido:
            nuevos_mensajes.append(item)
        else:
            mensajesAntiguos.append(item)
    return nuevos_mensajes,mensajesAntiguos,mensajesEnviados

    

def inicio(request): 
    todosPost=Post.objects.order_by('-fechaModificacion')
    cantidad=len(buscarmensaje(request)[0]) 
    mensajeIntermedio='Aquí encontraras los mejores lugares y recomendaciones para tus viajes por la patagonia!'     
    try:
       return render (request,'inicio.html',{'mensajeIntermedio':mensajeIntermedio,'todosPost':todosPost,'avatar':obtener_avatar(request),'mensaje':'Estas son las ultimas historias compartidas por los amantes de la aventura','cantidad':cantidad})
    except:
        return render (request,'inicio.html',{'mensajeIntermedio':mensajeIntermedio,'todosPost':todosPost,'mensaje':'Te invitamos a que te registres para poder compartir tus historias'}) 

def aboutMe(request): 
    cantidad=len(buscarmensaje(request)[0])    
    try:
       return render (request,'aboutMe.html',{'avatar':obtener_avatar(request),'cantidad':cantidad})
    except:
        return render (request,'aboutMe.html') 



def registro(request):
    if request.method =='POST':
        form=RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            nuevo_usuario=form.cleaned_data.get('username')
            form=AuthenticationForm()
            return render (request,'login.html',{'form':form,'mensaje':f'Usuario {nuevo_usuario} creado correctamente'})
        else:  
            return render(request, 'registro.html',{'mensaje':'falla usuario','form':form})
    else:
        form=RegistroForm()
        return render (request,'registro.html',{'form':form,'mensaje':'Registrate para poder formar parte de esta red de viajeros!'})

def login_usuario (request):
    todosPost=Post.objects.order_by('-fechaModificacion')

    if request.method=='POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
             nombre_usuario=form.cleaned_data.get('username')
             contrasenia=form.cleaned_data.get('password')
             usuario=authenticate(username=nombre_usuario,password=contrasenia)
            
             if usuario is not None:
                login(request, usuario)
                cantidad=len(buscarmensaje(request)[0]) 
                return render (request,'inicio.html',{'mensajeIntermedio':'Bienvenido de nuevo','todosPost':todosPost,'avatar':obtener_avatar(request),'mensaje':'Estas son las ultimas historias compartidas por los amantes de la aventura','cantidad':cantidad})

             else:
                return render (request,'login.html',{'mensaje':'Usuario o contraseña incorrecto'})
        else:
            return render (request,'login.html',{'mensaje':'Usuario o contraseña incorrecto','form':form})
    else:
        form=AuthenticationForm()
        return render (request,'login.html',{'form':form,'mensaje':'Ingresa para poder compartir tus historias!'})

@login_required
def editarperfil (request):
    todosPost=Post.objects.order_by('-fechaModificacion')
    cantidad=len(buscarmensaje(request)[0])  
    estado=0
    usuario=request.user
    perfil=Perfil.objects.get(user=usuario)
    
    if request.method=='POST':
        form=EditarUserForm(request.POST)
        form1=EditarPerfilForm(request.POST,request.FILES)
        if form.is_valid():
            info=form.cleaned_data
            usuario.first_name=info['first_name']
            usuario.last_name=info['last_name']
            usuario.email=info['email']
            usuario.password1=info['password1']
            usuario.password2=info['password2']
            usuario.save()
            estado=10           
        else:
            estado=20        
        if form1.is_valid():
            perfil=Perfil(user=request.user, imagen=request.FILES['imagen'],sitio_web=form1.cleaned_data['sitio_web'],descripcion=form1.cleaned_data['descripcion'])
    
            perfilanterior=Perfil.objects.filter(user=request.user)
            if len(perfilanterior)>0:
                perfilanterior[0].delete()
            perfil.save()
            estado+=1
        else:
            estado+=2
        if estado==11:
            return render (request,'inicio.html',{'todosPost':todosPost,'mensaje':'Usuario y avatar editado correctamente','avatar':obtener_avatar(request),'cantidad':cantidad})
        elif estado==12:
            return render (request,'inicio.html',{'todosPost':todosPost,'mensaje':'Solo el usuario fue editado correctamente','avatar':obtener_avatar(request),'cantidad':cantidad})
        elif estado ==21:
            return render (request,'inicio.html',{'todosPost':todosPost,'mensaje':'Solo el avatar fue editado correctamente','avatar':obtener_avatar(request),'cantidad':cantidad})
        else:
            return render (request,'inicio.html',{'todosPost':todosPost,'mensaje':'Fallo la edicion del perfil','avatar':obtener_avatar(request),'cantidad':cantidad})
    else:
        form=EditarUserForm(instance=usuario)
        form1=EditarPerfilForm({'descripcion':perfil.descripcion,'sitio_web':perfil.sitio_web})
        return render(request,'editarperfil.html',{'form':form,'form1':form1,'avatar':obtener_avatar(request),'cantidad':cantidad})

@login_required
def verperfil(request):
    cantidad=len(buscarmensaje(request)[0])  
    usuario=request.user

    try:
        modelo=Perfil.objects.filter(user=usuario)[0]
        return render(request,'verperfil.html',{'usuario':usuario,'modelo':modelo,'avatar':obtener_avatar(request),'mensaje':'','cantidad':cantidad})
    except:
        modelo=Perfil(user=request.user,descripcion='Escribe algo sobre ti',sitio_web='enlaza tu sitio',imagen='avatars/avatar_defecto.jpg')
        modelo.save()
        return render(request,'verperfil.html',{'usuario':usuario,'modelo':modelo,'avatar':obtener_avatar(request),'mensaje':'','cantidad':cantidad})
    

    

def eliminarperfil(request):
    usuario=request.user 
    usuario.delete()
    todosPost=Post.objects.order_by('-fechaModificacion')  
    mensajeIntermedio='Usuario eliminado correctamente'
    mensaje='Lamentamos tu retiro, esperamos que vuelas pronto'
    return render (request,'inicio.html',{'mensajeIntermedio':mensajeIntermedio,'todosPost':todosPost,'mensaje':mensaje}) 


@login_required
def mensajeria(request):
    todosPost=Post.objects.order_by('-fechaModificacion')
    nuevo_mensaje=buscarmensaje(request)[0]
    mensajesAntiguos=buscarmensaje(request)[1]
    mensajesEnviados=buscarmensaje(request)[2]
    usuario=request.user
    if request.method=='POST':
        form=MensajeriaForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data  
            existe=User.objects.filter(username=info['receptor'])
            if len(existe)!=1:
                form=MensajeriaForm()    
                return render (request,'mensajeria.html',{'mensajesEnviados':mensajesEnviados,'cantidad':len(buscarmensaje(request)[0]),'form':form,'avatar':obtener_avatar(request),'mensaje':'Usuario no existe','nuevo_mensaje':nuevo_mensaje})
            else:
                mensaje= Mensajes(emisor=usuario.username,receptor=info['receptor'],cuerpo_mensaje=info['cuerpo_mensaje'],leido=False)
                mensaje.save()  
                return render (request,'inicio.html',{'todosPost':todosPost,'cantidad':len(buscarmensaje(request)[0]),'mensaje':'Mensaje enviado correctamente','avatar':obtener_avatar(request),'nuevo_mensaje':nuevo_mensaje})       
        else:
            form=MensajeriaForm()
            return render (request,'mensajeria.html',{'mensajesEnviados':mensajesEnviados,'cantidad':len(buscarmensaje(request)[0]),'mensaje':'Fallo el envio del mensaje','avatar':obtener_avatar(request),'nuevo_mensaje':nuevo_mensaje})
    else:
        form=MensajeriaForm()
        return render (request,'mensajeria.html',{'mensajesEnviados':mensajesEnviados,'cantidad':len(buscarmensaje(request)[0]),'form':form,'avatar':obtener_avatar(request),'nuevo_mensaje':nuevo_mensaje,'mensajesAntiguos':mensajesAntiguos})



def leermensaje(request, id):
    mensajeActual=Mensajes.objects.get(id=id)
    mensajeActual.leido=True
    mensajeActual.save()
    mensajesEnviados=buscarmensaje(request)[2]
    nuevo_mensaje=buscarmensaje(request)[0]
    mensajesAntiguos=buscarmensaje(request)[1]
    form=MensajeriaForm()
    return render (request,'mensajeria.html',{'mensajesEnviados':mensajesEnviados,'cantidad':len(buscarmensaje(request)[0]),'avatar':obtener_avatar(request),'form':form,'nuevo_mensaje':nuevo_mensaje,'mensajeActual':mensajeActual,'mensajesAntiguos':mensajesAntiguos})

def responderMensaje(request, id):
    mensajeActual=Mensajes.objects.get(id=id)
    mensajesEnviados=buscarmensaje(request)[2]
    nuevo_mensaje=buscarmensaje(request)[0]
    mensajesAntiguos=buscarmensaje(request)[1]

    form=MensajeriaForm({'receptor':mensajeActual.emisor})
    return render (request,'mensajeria.html',{'mensajesEnviados':mensajesEnviados,'cantidad':len(buscarmensaje(request)[0]),'avatar':obtener_avatar(request),'form':form,'nuevo_mensaje':nuevo_mensaje,'mensajeActual':mensajeActual,'mensajesAntiguos':mensajesAntiguos})
            

def vermensaje(request, id):
    mensajeActual=Mensajes.objects.get(id=id)
    mensajesEnviados=buscarmensaje(request)[2]
    nuevo_mensaje=buscarmensaje(request)[0]
    mensajesAntiguos=buscarmensaje(request)[1]
    form=MensajeriaForm()
    return render (request,'mensajeria.html',{'mensajesEnviados':mensajesEnviados,'cantidad':len(buscarmensaje(request)[0]),'avatar':obtener_avatar(request),'form':form,'nuevo_mensaje':nuevo_mensaje,'mensajeActual':mensajeActual,'mensajesAntiguos':mensajesAntiguos})

    
