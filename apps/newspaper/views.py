from django.shortcuts import render
from django.http import JsonResponse
from .models import Noticia

# Create your views here.
def index(request):
    return render(request, 'newspaper/index.html')

def lista_noticias(request):
    todas_noticias = Noticia.objects.all()
    return render(request, 'newspaper/index.html', {'todas_noticias': todas_noticias})

def detalle_noticia(request, noticia_id):
    noticia = Noticia.objects.get(pk=noticia_id)
    data = {
        "id": noticia.id,
        "titulo": noticia.titulo,
        "fecha": noticia.fecha,
        "contenido": noticia.contenido,
        "autor": noticia.autor,
        "imagen": noticia.imagen.url
    }
    return JsonResponse(data)