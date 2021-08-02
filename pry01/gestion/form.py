from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from gestion.models import Usuario

class registro_usuario(UserCreationForm):
    class Meta:
        model= Usuario
        fields= ['username','nombres','apellidos','email','usuario_activo','dni_trabajador']
        labels = {
                'username': 'Nombre de usuario',
                'nombres': 'Nombre',
                'apellidos': 'Apellidos',
                'email':'Correo',
                'usuario_activo' : 'Activo',
                'dni_trabajador':'Dni'
        }

        
