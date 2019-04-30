from django import forms
from .models import Genero, Autor

class LibroForm(forms.Form):
    titulo = forms.CharField(label='Titulo del libro', max_length=100)
    sinopsis = forms.CharField(label='Sinopsis', widget=forms.Textarea)
    autor = forms.ModelChoiceField(queryset=Autor.objects.all())
    genero = forms.ModelChoiceField(queryset=Genero.objects.all())