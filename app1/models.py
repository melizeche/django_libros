from django.db import models

# Un Autor puede tener varios libros
# Un libro puede tener un autor
# Un Libro puede tener varios Generos
# Un Genero puede pertenecer a varios libros

# null=True, blank=True hace que el campo sea opcional
class Autor(models.Model):
    nombre = models.CharField(max_length=120)
    nacionalidad =  models.CharField(max_length=120, null=True, blank=True)
    
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    nombre = models.CharField(max_length=120)
    sinopsis = models.TextField(null=True, blank=True)
    #ForeignKey('NombreDeLaTabla') relaciona un autor a un libro
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True, blank=True)
    #ManyToManyField('NombreDeLaTabla') relaciona un libro con uno o mas generos
    generos = models.ManyToManyField('Genero')
    
    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre_genero = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_genero