from django.shortcuts import render
from django.http import HttpResponse

from .models import Libro

# Create your views here.


def home(request):
    return render(request, "index.html")


def busqueda(request):
    # Obtenemos los parametros enviados por el formulario, es un diccionario
    parametros_form = request.GET 
    # guardamos en titulo_a_buscar el valor de la clave "titulo"(name=titulo en el form html)
    titulo_a_buscar = parametros_form.get("titulo")
    #imprimimos en la terminal
    print("Titulo:", titulo_a_buscar)
    # Retornamos el parametro/argumento buscado
    return HttpResponse("HOLA estas buscando: " + str(titulo_a_buscar))


def lista_libro(request):
    #obtenemos todos los Objetos Libro
    todos = Libro.objects.all()
    # Retornamos usando el template lista.html y le pasamos al template
    # el diccionario {"libros":ListaDeTodoslosLibros}
    return render(request, "lista.html", {"libros": todos})


def busqueda2(request):
    # Obtenemos los parametros enviados por el formulario, es un diccionario
    parametros_form = request.GET 
    # guardamos en titulo_a_buscar el valor de la clave "titulo"(name=titulo en el form html)
    titulo_a_buscar = parametros_form.get("titulo")
    #imprimimos en la terminal (Opcional)
    print("Titulo:", titulo_a_buscar)
    # Obtenemos los elementos Libro que en el campo nombre contengan el
    # el parametro buscado
    resultado_busqueda = Libro.objects.filter(nombre__icontains=titulo_a_buscar)
    
    return render(request, "lista.html", {"libros": resultado_busqueda})

