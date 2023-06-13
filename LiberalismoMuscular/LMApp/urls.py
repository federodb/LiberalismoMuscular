from django.urls import path
from LMApp import views


urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),
    path('buscarutina/', views.buscarutina, name="buscarutina"),
    path('curso/', views.curso, name="Curso"),
    path('rutinas/', views.rutinas, name="Rutinas"),
    path('alimentos/', views.alimentos, name="Alimentos"),
    path('contacto/', views.contacto, name="Contacto"),
    path('cursoFormulario/', views.cursoForm, name="CursoForm"),
    path('rutinasFormulario/', views.rutinasForm, name="RutinasForm"),
    path('alimentosFormulario/', views.alimentosForm, name="AlimentosForm"),
    path('listarutinas/', views.listarutina, name="listarutina"),
]