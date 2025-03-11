from django.urls import path
from .views import index, lista_tareas, marcar_completada

urlpatterns = [
    path('', index, name='tareas_index'),
    path('lista/', lista_tareas, name='lista_tareas'),
    path('completar/<int:tarea_id>/', marcar_completada, name='marcar_completada'),
]
