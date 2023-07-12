from django.shortcuts import render, redirect
from .models import Producto
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RegistroUserForm
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

def login(request):
    return render(request, 'login.html')


def registrarCarrito(request):
    if request.method == 'POST':
        codigo = request.POST.get('txtCodigo')
        nombre = request.POST.get('txtNombre')
        precio = request.POST.get('numPrecio')
        cantidad = request.POST.get('numCantidad')

        producto = Producto.objects.create(codigo=codigo, nombre=nombre, precio=precio, cantidad=cantidad)
        return redirect('/')
    else:
        # Manejar caso cuando el método de solicitud no es POST
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

def registrar(request):
    data={
        'form':RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], 
                    password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect ('index')
        data["form"] = formulario
    return render(request, 'registration/registrar.html',data)