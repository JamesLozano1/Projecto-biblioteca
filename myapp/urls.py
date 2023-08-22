from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('biblioteca', views.biblioteca, name='biblioteca'),
    path('libro', views.libro, name='libro'),
    path('crear_Biblioteca', views.crear_Biblioteca, name='crear_Biblioteca'),
    path('crear_libro', views.crear_Libro, name='crear_libro'),
]