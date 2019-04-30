from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('lista/', views.lista_libro),
    path('busqueda/', views.busqueda),
    path('busqueda2/', views.busqueda2),
    path('crearautor/', views.crear_autor),
    path('crearlibro/', views.crear_libro),


]
