
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    

    path('',views.mostrar_index, name='index'),
    path('mostrar_gallery/', views.mostrar_gallery, name='Galeria'),
    path('mostrar_contact/', views.mostrar_contact, name='Contacto'),
    path('buscar_post/', views.buscar_post, name='buscar'),
    path('crear_post/', views.crear_post, name='crear'),
    path('cursoPost/', views.cursoPost, name='CursoPost'),
    path('buscador/', views.buscador, name='buscar'),
    path('mostrarPost/', views.PosteoList.as_view(), name='mostrarpost'),
    path('PosteoDetail/<pk>', views.PosteoDetail.as_view(), name='Detail'),
    path('base/', views.base, name='base')
]
