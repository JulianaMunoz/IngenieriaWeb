from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tarea

# Create your views here.
def index(request):
    return render(request, 'tareas/index.html')

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})

def marcar_completada(request, tarea_id):
    tarea = Tarea.objects.get(pk=tarea_id)
    tarea.completada = not tarea.completada
    tarea.save()
    return redirect('lista_tareas')