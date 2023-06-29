from django.urls import path,include
from django.db import models
from .views import index, Nacionales, Internacionales, form, mapa, carrito, registrarCarrito

urlpatterns = [
    path('', index, name='index'),
    path('Nacionales/', Nacionales, name='Nacionales'),
    path('Internacionales/', Internacionales, name='Internacionales'),
    path('form/', form, name='form'),
    path('mapa/', mapa, name='mapa'),
    path('carrito/', carrito, name='carrito'),
    path('registrarCarrito/', registrarCarrito, name='registrarCarrito'),

]




