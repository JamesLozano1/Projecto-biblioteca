from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Biblioteca, Libro
from .forms import CreatenewBiblioteca

def index( request ):
    title = '¡¡Projecto Biblioteca DJango!!'
    return render( request, 'index.html', {
        'title': title,
    })

def biblioteca( request ):
    biblioteca = list(Biblioteca.objects.values())
    titulo = 'Biblioteca:'
    return render(request, 'Biblioteca/biblioteca.html',{
        'titulo':titulo,
        'biblioteca':biblioteca,
    })

def crear_Biblioteca( request ):
    if request.method == 'GET':
        return render( request, 'Biblioteca/biblioteca.html', {
            'form':CreatenewBiblioteca(),
        })
    else:
        nombre = request.POST['nombre']
        ubicacion = request.POST['ubicacion']
        Biblioteca.objects.create(nombre=nombre, ubicacion=ubicacion)
        return redirect('/biblioteca')