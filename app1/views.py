from django.shortcuts import render
from django.http import HttpResponse

from .models import Libro, Autor, Genero
from .forms import LibroForm

# Create your views here.


def home(request):
    form = LibroForm()

    return render(request, "index.html", {"formulario":form})


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

def crear_autor(request):
    nombre_autor = request.GET.get("nombre")
    nacionalidad = request.GET.get("nacionalidad")
    print(nombre_autor,nacionalidad)

    autor_nuevo = Autor(nombre=nombre_autor, nacionalidad=nacionalidad)
    autor_nuevo.save()

    return HttpResponse("Se creo el autor " + nombre_autor)


def crear_libro(request):
    if request.method=='POST':
        print(request.POST)
        parametros = request.POST
        titulo = parametros.get("titulo")
        sinopsis = parametros.get("sinopsis")
        genero = parametros.get("genero")
        autor = parametros.get("autor")
        obj_autor = Autor.objects.get(id=autor)
        qs_genero = Genero.objects.all()
        
        libro_nuevo = Libro(nombre=titulo, sinopsis=sinopsis, autor=obj_autor)#, generos=qs_genero)
        libro_nuevo.save()

        return HttpResponse("Se creo el libro "+ titulo)
        
    else:
        form = LibroForm()
    
    return render(request, 'formu.html', {"formu":form})
