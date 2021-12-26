from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):

	return render(request, "ProyectofinalApp/inicio.html")


def posts(request):

 	return render(request, "ProyectofinalApp/posts.html")


