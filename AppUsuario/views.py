from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .forms import PosteoForm
from .models import Posteo

# Create your views here.

def mostrar_index(request):
    return render(request,'index.html')

def mostrar_gallery(request):
    return render(request,'gallery.html')
    
def mostrar_contact(request):
    
    return render(request,'contact.html')


def cursoPost(request):
    
    return render(request,'Posts.html')



def crear_post(request):

    if request.method == 'POST':

        posteo = PosteoForm(request.POST)

        print('posteo')

        if posteo.is_valid():
        
            data = posteo.cleaned_data
        
            posteo  = Posteo (titulo=data['titulo'], texto=data['texto'])

            posteo.save()

            return render(request,'index.html')

    else:

        posteo = PosteoForm()

        print('formulario')

    return render(request,'Posts.html',{'posteo':posteo})


def buscar_post(request):

    return render(request,'buscador.html')



def buscador (request):
    if request.GET.get ('titulo', False):

        titulo  = request.GET ['titulo']
        
        post = Posteo.objects.filter(titulo__icontains=titulo)

        return render (request, 'buscador.html',{'post':post})
        
    else:
        respuesta = 'no hay datos'
    
    return render (request, 'buscador.html', {'respuesta':respuesta})
    


class PosteoList(ListView):

    model = Posteo
    template_name = 'mostrar_post.html'

class PosteoDetail(DetailView):

    model = Posteo
    template_name = 'posteo_detalle.html' 


def base(request):

    return render(request,'base.html')