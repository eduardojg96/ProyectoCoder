from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.
def curso(self):
    curso=Curso(nombre="Django",comision=96969)
    curso.save()
    texto=f"curso creado: {curso.nombre} {curso.comision}"
    return HttpResponse(texto)