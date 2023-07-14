from django.shortcuts import render

# Create your views here.
from myApp2.models import Autor, Libro

def detalle_autor(request, autor_id):
    autor = Autor.objects.get(pk=autor_id)
    libros = autor.libro_set.all()

    context = {
        'autor': autor,
        'libros': libros
    }
    return render(request, 'base.html', context)