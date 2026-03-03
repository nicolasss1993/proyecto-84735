from django.shortcuts import render
from alumnos.models import Alumnos

# Create your views here.
def inicio(request):
    return render(request, "alumnos/inicio.html")


def listar_alumnos(request):
    alumnos_query = Alumnos.objects.all() # list(QuerySet[Alumno, Alumno2, ...])
    context = {
        "alumnos_list": alumnos_query
    }
    return render(request, "alumnos/alumnos_list.html", context)

def ver_alumno(request, nro_alumno):
    try:
        alumno = Alumnos.objects.get(nro_alumno=nro_alumno)
    except Alumnos.DoesNotExist:
        return render(request, "error_404.html")
    context = {
        "alumno" : alumno
    }
    return render(request, "alumnos/ver_alumno.html", context)
