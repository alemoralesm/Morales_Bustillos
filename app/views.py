from django.shortcuts import render, redirect
from .models import Producto

def carrito(request):
    producto = Producto.objects.all()
    return render(request, "carrito.html", {"producto": producto})

def index(request):
    return render(request, 'index.html')

def Nacionales(request):
    return render(request, 'Nacionales.html')

def Internacionales(request):
    return render(request, 'Internacionales.html')

def form(request):
    return render(request, 'form.html')

def mapa(request):
    return render(request, 'mapa.html')




def registrarCarrito(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    precio = request.POST['numPrecio']
    cantidad = request.POST['numCantidad']

    producto = Producto.objects.create(codigo=codigo, nombre=nombre, precio=precio, cantidad=cantidad)
    return redirect('/')

def edicionCarrito(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    return render(request, "edicionCarrito.html", {"producto": producto})

def editarCarro(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    precio = request.POST['numPrecio']
    cantidad = request.POST['numCantidad']

    producto = Producto.objects.get(codigo=codigo)
    producto.nombre = nombre
    producto.precio = precio
    producto.cantidad = cantidad
    producto.save()

    return redirect('/')

def eliminarCarro(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect('/')
