from django.db import models

# Create your models here.
class Foto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='fotos/')

    def __str__(self):
        return self.titulo