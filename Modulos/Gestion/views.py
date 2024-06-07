from django.shortcuts import render

def index(request):
    return render(request, 'gestion/index.html')

def productos(request):
    return render(request, 'gestion/productos.html')

def clientes(request):
    return render(request, 'gestion/clientes.html')

def contacto(request):
    return render(request, 'gestion/contacto.html')

