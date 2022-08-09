from django.shortcuts import render, redirect, get_object_or_404
from django.urls import is_valid_path
from isort import file
from .models import Producto
from .forms import ContactoForm, ProductoForm

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html',data)

def contacto(request):
    data= {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] ="contacto guardado"
        else:
            data["form"] = formulario
    return render(request, 'app/contacto.html', data)

def galeria(request):
    return render(request, 'app/galeria.html')



def agregar_producto(request):

    data= {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'app/producto/agregar.html', data)

def listar_productos(request):
    productos = Producto.objects.all()

    data= {
        'productos': productos
    }
    return render(request, 'app/producto/listar.html',data)


def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data ={
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
        data["form"] = formulario

    return render(request, 'app/producto/modificar.html', data)


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar_productos")