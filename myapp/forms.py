from django import forms
from .models import Biblioteca


class CreatenewLibro(forms.Form):
    titulo = forms.CharField(label='Ingrese el titulo del Libro', max_length=50)
    ISBN = forms.CharField(label='Ingrese el ISBN del Libro', max_length=13)
    autor = forms.CharField(label='Ingrese el nombre del autor', max_length=50) 
    estado = forms.CharField(label='Ingrese el estado del Libro', max_length=8)
    
    bibliotecas = forms.ModelChoiceField(label='Biblioteca', queryset=Biblioteca.objects.all())

class CreatenewBiblioteca(forms.Form):
    nombre = forms.CharField(label='Ingrese el nombre de la Biblioteca', max_length=50)
    ubicacion = forms.CharField(label='Ingrese la ubicacion de la biblioteca', widget=forms.TextInput)