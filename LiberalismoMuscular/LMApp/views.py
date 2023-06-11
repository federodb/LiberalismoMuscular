from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "LMApp/inicio.html")

def iniciarsesion(request):
    return render(request, "LMApp/iniciosesion.html")

def crearcuenta(request):
    return render(request, "LMApp/crearcuenta.html")

def quienesomos(request):
    return render(request, "LMApp/quienessomos.html")

def contacto(request):
    return render(request, "LMApp/contacto.html")

def blog(request):
    return render(request, "LMApp/blog.html")