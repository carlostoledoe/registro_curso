from django.shortcuts import render
from django.http import HttpResponse
from main.services import *

# Create your views here.
def test(request):
    crear_curso('SQL', 'Curso SQL', 2)
    crear_curso('TRT', 'Taror Avanzado', 3)
    # crear_estudiante('11.111.111-1', 'Juanito', 'Diaz', '1990-10-10')
    agrega_cursos_a_estudiante('SQL', '11.111.111-1')
    agrega_cursos_a_estudiante('TRT', '11.111.111-1')
    # crear_direccion('La Calle', '356', 'Quilpué', 'v', '11.111.111-1')
    # agrega_profesor_a_curso('44.444.444-4', 'PYT')
    # crear_profesor('77.777.777-7', 'Juanzo', 'Lolo')
    return HttpResponse('ok')