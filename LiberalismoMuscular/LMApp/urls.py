from django.urls import path
from LMApp import views


urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),
    path('iniciosesion/', views.iniciarsesion, name="InicioSesion"),
    path('crearcuenta/', views.crearcuenta, name="CrearCuenta"),
    path('blog/', views.blog, name="Blog"),
    path('quienessomos/', views.quienesomos, name="QuienesSomos"),
    path('contacto/', views.contacto, name="Contacto")
]