from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField(blank=True, null=True)
    autor = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='noticias/')

    def __str__(self):
        return self.titulo