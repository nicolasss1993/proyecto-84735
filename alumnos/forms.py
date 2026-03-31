from django import forms
from .models import Alumnos
#from alumnos.models import Alumnos


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ["nombre", "apellido", "fecha_de_nacimiento", "dni", "email", "nro_alumno"]
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "nro_alumno": forms.NumberInput(attrs={'class': 'form-control'}),
            "apellido": forms.TextInput(attrs={'class': 'form-control'}),
            "fecha_de_nacimiento": forms.DateInput(attrs={'class': 'form-control'}),
            "dni": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'})
        }
        error_messages = {
            "nro_alumno": {
                'unique': "Numero de alumno en uso."
            },
            "dni": {
                'unique': "Ya tenemos un alumno con este dni!!!"
            }
        }


class AlumnoUpdateForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ["nombre", "apellido", "fecha_de_nacimiento", "dni", "email"]
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "apellido": forms.TextInput(attrs={'class': 'form-control'}),
            "fecha_de_nacimiento": forms.DateInput(attrs={'class': 'form-control'}),
            "dni": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'})
        }
        error_messages = {
            "dni": {
                'unique': "Ya tenemos un alumno con este dni!!!"
            }
        }
        

class AlumnoDosForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    apellido = forms.CharField(max_length=100, label="Apellido")
    nro_alumno = forms.IntegerField(label="Numero de Alumno")
    fecha_de_nacimiento = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Fecha de nacimiento"
    )
    dni = forms.CharField(max_length=12, label="D.N.i")
    email = forms.EmailField(label="Email")

    def clean_nro_alumno(self):
        nro_alumno = self.cleaned_data["nro_alumno"]
        if Alumnos.objects.filter(nro_alumno=nro_alumno).exists():
            raise forms.ValidationError("Numero de alumno EXISTENTE")
        return nro_alumno
