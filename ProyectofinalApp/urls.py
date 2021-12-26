from django.urls import path

from ProyectofinalApp import views 

urlpatterns = [
     
    path('',views.inicio, name="Inicio"),

]
