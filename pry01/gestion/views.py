from django.urls import reverse_lazy

from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView

from django.contrib.auth import authenticate

from django.http import HttpResponse

from django.contrib import messages

from gestion.models import Trabajador, Usuario

from gestion.form import registro_usuario

# Create your views here.
  


def Inicio(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def medicamentos(request):
    return render(request,'medicamentos.html')

def trabajadores(request):
    trab=Trabajador.objects.all().select_related()
    return render(request,'trabajadores.html',{"trabajadores":trab})
   

def usuarios2(request):
    usuarios=User.objects.all()
    return render(request,'formuser.html',{"usuarios":usuarios})

def buscar_trabajador(request):
    if request.GET['dni']:
        doc= request.GET['dni']
        trab= Trabajador.objects.filter(dni=doc)
        if trab:
            return render(request,'formuser.html',{"trabajador":trab})
        else:
            return HttpResponse("El empleado no existe")
    else:
        return HttpResponse("Ingrese un dni a buscar")


def registrar_trabajadores(request):
    if len(request.POST['dni'])>0 and len(request.POST['nombres'])>0 and len(request.POST['apellidos'])>0 and len(request.POST['correo'])>0 and  len(request.POST['telefono'])>0 and  len(request.POST['direccion'])>0:
        doc = request.POST['dni']
        nom= request.POST['nombres']
        ape= request.POST['apellidos']
        email= request.POST['correo']
        telef= request.POST['telefono']
        direc= request.POST['direccion']
        objT=Trabajador(dni=doc,nombre=nom,apellido=ape, email=email,telefono=telef,direccion=direc)
        objT.save()
        trab=Trabajador.objects.all()
        messages.add_message(request=request, level=messages.SUCCESS, message="¡Operación exitosa! Trabajador registrado correctamente")
        return render(request,'trabajadores.html',{"trabajador":trab})
    else:
        messages.add_message(request=request, level=messages.INFO , message="Complete Todos los campos")
        trab=Trabajador.objects.all()
        return render(request,'trabajadores.html',{"trabajador":trab})

def eliminar_trabajador(request):
    if request.GET['bntEli']:
        dni=request.GET['bntEli']
        t=Usuario.objects.filter(dni_trabajador=dni).delete()
        trab=Trabajador.objects.filter(dni=dni).delete()
        trab=Trabajador.objects.all() 
        return render(request,'trabajadores.html',{"trabajador":trab})

class user_registro(CreateView):
    model=Usuario
    form_class=registro_usuario
    usuarios=Usuario.objects.all()
    template_name='formuser.html'
    success_url=reverse_lazy('usuarios')

class user_list(ListView):
    model=Usuario
    template_name='usuarios.html'
    


    
    
    


    
    
    




    






    




