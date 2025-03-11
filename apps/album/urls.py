from django.urls import path
from .views import index, lista_fotos

urlpatterns = [
    path('', index, name='album_index'),
    path('lista/', lista_fotos, name='lista_fotos'),  
]
