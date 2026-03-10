from django.shortcuts import render, redirect
from alumnos.models import Alumnos
from alumnos.forms import AlumnoForm

# Create your views here.
def inicio(request):
    return render(request, "alumnos/inicio.html")


def listar_alumnos(request):
    nombre = request.GET.get("nombre")
    alumnos_query = Alumnos.objects.all()[:20] # list(QuerySet[Alumno, Alumno2, ...])
    if nombre is not None:
        alumnos_query = Alumnos.objects.filter(
            nombre__icontains=nombre
        )
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

# GET - Pido informacion
# POST - Agregar informacion nueva. / Modificar informacion existente en la base de datos.
# DELETE - Eliminar informacion
# PUT - Actualizar informacion (Todo en la base de datos.)
def crear_alumno(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumnos_list')
    else:
        form = AlumnoForm()
    
    return render(request, "alumnos/crear_alumno.html", {
        "form": form
    })
