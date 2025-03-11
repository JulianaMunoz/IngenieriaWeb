from django.db import models

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateTimeField()
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo