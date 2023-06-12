from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso, Rutinas, Alimentos
from .forms import *

# Create your views here.

def inicio(request):
    return render(request, "LMApp/inicio.html")

def iniciarsesion(request):
    return render(request, "LMApp/iniciosesion.html")

def curso(request):
    return render(request, "LMApp/curso.html")

def cursoForm(request):

    if request.method == 'POST':

        form = CursoFormulario(request.POST)

        if form.is_valid():
            informacion = form.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "LMApp/inicio.html")
    else:
            form = CursoFormulario()

    return render(request, "LMApp/cursoForm.html", {"formulario": form})

def alimentos(request):
    return render(request, "LMApp/alimentos.html")

def alimentosForm(request):

    if request.method == 'POST':

        form = AlimentosFormulario(request.POST)

        if form.is_valid():
            informacion = form.cleaned_data
            alimentos = Alimentos(nombre=informacion["alimento"], proteina=informacion["proteinas"])
            alimentos.save()
            return render(request, "LMApp/inicio.html")
    else:
            form = AlimentosFormulario()

    return render(request, "LMApp/alimentosForm.html", {"formulario": form})

def contacto(request):
    return render(request, "LMApp/contacto.html")

def rutinas(request):
    return render(request, "LMApp/rutinas.html")

def rutinasForm(request):

    if request.method == 'POST':

        form = RutinasFormulario(request.POST)

        if form.is_valid():
            informacion = form.cleaned_data
            rutina = Rutinas(nombre=informacion["rutina"], rutina=informacion["ejercicios"])
            rutina.save()
            return render(request, "LMApp/inicio.html")
    else:
            form = RutinasFormulario()

    return render(request, "LMApp/rutinaForm.html", {"formulario": form})

def buscarutina(request):
    return render(request, "LMApp/buscarutina.html")

def buscar(request):

    if request.GET["tipo"]:
        
        tipo = request.GET['tipo']
        ejercicios = Rutinas.objects.filter(nombre__icontains=tipo)

        return render(request, "LMApp/listarutinas.html", {"Tipo de rutina":tipo,"Ejercicios":ejercicios})
    
    else:
        
        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)