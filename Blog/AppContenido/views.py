from django.shortcuts import render
from AppUser.views import buscarmensaje, obtener_avatar
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from datetime import datetime

def buscarPost(request):
    misPost=[]
    todosPost=[]
    misPost=Post.objects.filter(user=request.user)
    todosPost=Post.objects.order_by('-fechaModificacion')
    return misPost,todosPost

@login_required
def nuevoPost(request): 
    cantidad=len(buscarmensaje(request)[0])  
    if request.method =='POST':
        form=crearPost(request.POST,request.FILES)      
        if form.is_valid():
            info=form.cleaned_data
            post=Post(
                    titulo=info['titulo'],
                    subtitulo=info['subtitulo'],
                    cuerpo=info['cuerpo'],
                    autor=request.user,
                    fechaCreacion=datetime.now(),
                    fechaModificacion=datetime.now(),
                    imagen=request.FILES['imagen'],
                    user=request.user
                    )    
            post.save()
            return render (request,'inicio.html',{'todosPost':buscarPost(request)[1],'mensaje':'Post creado correctamente','avatar':obtener_avatar(request),'cantidad':cantidad})
        else:
            return render (request,'Posteos.html',{'form':form,'avatar':obtener_avatar(request),'mensaje':'Falla al cargar el post','cantidad':cantidad})
    else:
        form=crearPost()
        return render (request,'Posteos.html',{'misPost':buscarPost(request)[0],'todosPost':buscarPost(request)[1],'form':form,'avatar':obtener_avatar(request),'mensaje':'MMMensaje','cantidad':cantidad})

def leerPost(request, id):
    cantidad=len(buscarmensaje(request)[0]) 
    postActual=Post.objects.get(id=id)
    return render (request,'leerPosteos.html',{'mensaje':'Post editados recientemente','postActual':postActual,'todosPost':buscarPost(request)[1],'avatar':obtener_avatar(request),'cantidad':cantidad})

def eliminarPost(request, id):
    cantidad=len(buscarmensaje(request)[0]) 
    postActual=Post.objects.get(id=id)
    postActual.delete()
    form=crearPost()
    return render (request,'Posteos.html',{'misPost':buscarPost(request)[0],'todosPost':buscarPost(request)[1],'form':form,'avatar':obtener_avatar(request),'mensaje':'MMMensaje','cantidad':cantidad})


def editarPost(request, id):
    todosPost=Post.objects.order_by('-fechaModificacion')
    cantidad=len(buscarmensaje(request)[0])   
    postActual=Post.objects.get(id=id)

    if request.method =='POST':
        form=crearPost(request.POST,request.FILES)      
        if form.is_valid():
            info=form.cleaned_data     
            postActual.titulo=info['titulo']
            postActual.subtitulo=info['subtitulo']
            postActual.cuerpo=info['cuerpo']
            postActual.fechaModificacion=datetime.now()
            postActual.imagen=request.FILES['imagen']                     
            postActual.save()
            return render (request,'inicio.html',{'todosPost':todosPost,'avatar':obtener_avatar(request),'mensajeIntermedio':'Post editado correctamente','cantidad':cantidad})
        else:
            form=crearPost({'titulo':postActual.titulo,'subtitulo':postActual.subtitulo,'cuerpo':postActual.cuerpo})
            return render (request,'editarPost.html',{'misPost':buscarPost(request)[0],'postActual':postActual,'form':form,'avatar':obtener_avatar(request),'mensaje':'Falla al editar el post','cantidad':cantidad})
    else:
        form=crearPost({'titulo':postActual.titulo,'subtitulo':postActual.subtitulo,'cuerpo':postActual.cuerpo})
        return render (request,'editarPost.html',{'misPost':buscarPost(request)[0],'postActual':postActual,'form':form,'avatar':obtener_avatar(request),'mensaje':'MMMensaje','cantidad':cantidad})

def todosPost(request):
    cantidad=len(buscarmensaje(request)[0])  
    todosPost=Post.objects.order_by('-fechaModificacion')
    try:
           return render(request,'todosPost.html',{'misPost':buscarPost(request)[0],'todosPost':todosPost,'avatar':obtener_avatar(request),'cantidad':cantidad})
    except:
        return render (request,'todosPost.html',{'todosPost':todosPost}) 

def buscarPostTitulo(request):
    cantidad=len(buscarmensaje(request)[0])  
    todosPost=Post.objects.order_by('-fechaModificacion')
    titulo=request.GET['titulo']
    if titulo!='':
         postEncontrados=Post.objects.filter(titulo__icontains=titulo).order_by('-fechaModificacion')
         return render(request,'busquedaPost.html',{'todosPost':todosPost,'misPost':buscarPost(request)[0],'postEncontrados':postEncontrados,'avatar':obtener_avatar(request),'cantidad':cantidad})
    else:
         return render(request,'busquedaPost.html',{'mensaje':'Campo de busqueda vacío','todosPost':todosPost,'misPost':buscarPost(request)[0],'avatar':obtener_avatar(request),'cantidad':cantidad})







  

