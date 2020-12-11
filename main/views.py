from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def frontPage(request):
    return render(request,'main/frontPage.html',{
        'text':'Inicio'
    })
def crearArticulo(request):
    formArt = formArticulo()
    if request.method == "POST":
        formArt = formArticulo(request.POST)
        if formArt.is_valid():#Validador
            datos = formArt.cleaned_data

            titulo = datos.get('titulo')
            contenido = datos.get('contenido')
            publico = datos.get('publico')
            imagen = datos.get('imagen')
            Articulo(
                titulo = titulo,
                contenido = contenido,
                publico = publico,
                imagen = imagen,
            ).save()
            
            return redirect("Ver Articulos")
    return render(request,"main/crearArticulo.html",{
        "text":"Crear Articulo",
        "formulario":formArt
    })
def visualizar(request):
    articulos = Articulo.objects.all()
    return render(request,"main/visualizar.html",{
        "text":"Visualizar",
        "articulos":articulos
    })