from django.urls import path
from LMApp import views


urlpatterns = [
    path('/', views.inicio),
]