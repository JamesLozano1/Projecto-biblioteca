from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Biblioteca, Libro
from .forms import CreatenewBiblioteca, CreatenewLibro

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

def libro( request ):
    titulo = 'Libro'
    libro = Libro.objects.all()
    return render( request, 'Libros/libro.html', {
        'titulo':titulo,
        'libro':libro,
    })

def crear_Libro( request ):
    if request.method == 'GET':
        return render( request, 'Libros/crear_Libro.html', {
            'form':CreatenewLibro(),
        })
    else:
        form = CreatenewLibro(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            autor = form.cleaned_data['autor']
            ISBN = form.cleaned_data['ISBN']
            estado = form.cleaned_data['estado']
            bibliotecas_id = form.cleaned_data['bibliotecas'].id
            biblioteca = Biblioteca.objects.get(id=bibliotecas_id)
            Libro.objects.create(titulo=titulo, autor=autor, ISBN=ISBN, estado=estado, bibliotecas=biblioteca)
            return redirect('/libro')
        # return render(request, 'Libros/crear_Libro.html', {
        #     'form': form,
        #     })

def crear_Biblioteca( request ):
    if request.method == 'GET':
        return render( request, 'Biblioteca/crear_Biblioteca.html', {
            'form':CreatenewBiblioteca(),
        })
    else:
        nombre = request.POST['nombre']
        ubicacion = request.POST['ubicacion']
        Biblioteca.objects.create(nombre=nombre, ubicacion=ubicacion)
        return redirect('/biblioteca')
