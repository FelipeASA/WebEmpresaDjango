from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# views de RRHH
# definimos que se redireccionen a los html que estan en la 
# carpeta templates

def index(request):
    # return HttpResponse("Pagina Index")
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("Pagina about")
    dato = {
        "Direccion":"Miguel Claro sn",
        "Fono":"9 8765 6321",
        "Email":"curso@douc.cl"
    }   # definimos un objeto dato
    contexto = {"info":dato} # definimos un objeto contexto
    # para enviarlos al template about.html
    return render(request, 'about.html', contexto)
