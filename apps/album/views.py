from django.shortcuts import render
from django.http import HttpResponse
from .models import Foto

# Create your views here.
def index(request):
    return render(request, 'album/index.html')

def lista_fotos(request):
    todas_fotos = Foto.objects.all()
    return render(request, 'album/index.html', {'todas_fotos': todas_fotos})