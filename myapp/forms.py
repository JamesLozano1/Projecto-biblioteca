from django import forms
from .models import Biblioteca

class CreatenewBiblioteca( forms.Form ):
    nombre = forms.CharField(label='Ingrese el nombre de la Biblioteca', max_length=50)
    ubicacion = forms.CharField(label='Ingrese la ubicacion de la biblioteca', max_length=50)


class CreatenewLibro( forms.Form ):
    titulo = forms.CharField(label='Ingrese el titulo del Libro', max_length=50)
    ISBN = forms.CharField(label='Ingrese el ISBN del Libro', max_length=13)
    autor = forms.CharField(label='Ingrese el nombre del autor', max_length=50) 
    estado = forms.CharField(label='Ingrese el estado del Libro', max_length=8)
    
    CHOICES = Biblioteca.objects.all()
    Biblioteca_id = forms.ModelChoiceField(label='Biblioteca', queryset=CHOICES)