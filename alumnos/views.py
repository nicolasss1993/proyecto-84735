from django.shortcuts import render, redirect, get_object_or_404
from alumnos.models import Alumnos
from alumnos.forms import AlumnoForm, AlumnoUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def inicio(request):
    return render(request, "alumnos/inicio.html")


@login_required
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

@login_required
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
@login_required
def crear_alumno(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            # Alumnos.objects.create(
            #     nombre=form.cleaned_data["nombre"],
            #     apellido=form.cleaned_data["apellido"],
            #     nro_alumno=form.cleaned_data["nro_alumno"],   CON forms.FORM
            #     fecha_de_nacimiento=form.cleaned_data["fecha_de_nacimiento"],
            #     dni=form.cleaned_data["dni"],
            #     email=form.cleaned_data["email"]
            # )
            form.save()  # CON forms.ModelForm
            return redirect('alumnos_list')
    else:
        form = AlumnoForm()
    
    return render(request, "alumnos/crear_alumno.html", {
        "form": form,
    })


@login_required
def actualizar_alumno(request, dni):
    alumno = get_object_or_404(Alumnos, dni=dni)
    if request.method == "POST":
        form = AlumnoUpdateForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect("alumnos_list")
    else:
        form = AlumnoUpdateForm(instance=alumno)

    context = {"form": form}
    return render(request, "alumnos/actualizar_alumno.html", context)

@login_required
def eliminar_alumno(request, dni):
    alumno = get_object_or_404(Alumnos, dni=dni)
    if request.method == "POST":
        alumno.delete()
        return redirect("alumnos_list")
    return redirect("alumno_list")

"""
C-reate / Crear
R-ead / Leer              REGISTROS EN BD
U-pdate / Actualizar
D-elete / Eliminar
"""