from django.db import models

class Biblioteca( models.Model ):
    nombre = models.CharField(help_text='Ingrese el nombre de la Biblioteca', max_length=50)
    ubicacion = models.CharField(help_text='Ingrese la ubicacion de la Biblioteca', max_length=50)
    def __str__( self ):
        return self.nombre

class Libro( models.Model ): 
    titulo = models.CharField(help_text='Ingrese el titulo del Libro', max_length=50)
    ISBN = models.CharField(max_length=13, help_text='Ingrese el ISBN del Libro')
    autor = models.CharField(help_text='Ingrese el nombre del autor', max_length=50)
    estado = models.CharField(help_text='Ingrese el estado del Libro', max_length=8)
    bibliotecas = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.titulo + " - " + self.bibliotecas.nombre