from django import forms

from apps.adopciones.models import Solicitud, Persona

class PersonaForms(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [

            'nombre',
            'apellidos',
            'edad',
            'telefono',
            'email',
            'domicilio',

        ]
        labels = {
            'nombre': 'Nombre',
            'apellidos':'Apellidos',
            'edad': 'Edad',
            'telefono': 'Numero telefonico',
            'email': 'Correo electronico',
            'domicilio': 'Direccion particular',
        }
        widgets = {

            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.Textarea(attrs={'class':'form-control'}),

        }


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [

            'numero_mascotas',
            'razones',

        ]
        labels = {

            'numero_mascostas':'Numero de mascotas',
            'razones': 'Razones para adoptar',


        }
        widgets={

            'numero_mascotas': forms.TextInput(attrs= {'class':'form-control'}),
            'razones' : forms.Textarea(attrs={'class':'form-control'})

        }

