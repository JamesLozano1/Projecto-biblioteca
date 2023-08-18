from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('biblioteca', views.biblioteca, name='biblioteca'),
    
]