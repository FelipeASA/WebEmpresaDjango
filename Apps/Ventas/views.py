from django.shortcuts import render, redirect
from django.http import HttpResponse

# importamos todos los modelos de Apps.Ventas
from Apps.Ventas.models import *
from Apps.Ventas.forms import *

# Create your views here.

def index(request):
    return HttpResponse("Index de Ventas")

def productos(request):
    # leer los productos del modelo - tabla Ventas_producto
    # select * from Ventas_producto
    # datos = Producto.objects.raw('select * from Ventas_producto')
    # datos = Producto.objects.filter(id=3)
    datos = Producto.objects.all()
    print(datos) # muestra en consola
    contexto = {"productos": datos} 
    # nombre que usaremos en el template "productos"
    return render(request, 'productos.html', contexto)

def venta_view(request):
    if request.method == "POST":
        form = VentaProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form=VentaProductoForm()

    contexto = {'form': form}
    return render(request, 'venta_formulario.html', contexto)

