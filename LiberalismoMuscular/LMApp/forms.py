from django import forms

# Creación de formularios:

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class RutinasFormulario(forms.Form):
    rutina = forms.CharField(max_length=40)
    ejercicios = forms.CharField(widget=forms.Textarea())

class AlimentosFormulario(forms.Form):
    alimento = forms.CharField(max_length=40)
    proteinas = forms.CharField(max_length=20)

class BuscaRutina(forms.Form):
    rutina = forms.CharField()