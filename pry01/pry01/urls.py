"""pry01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,logout_then_login
from gestion.views import Inicio,dashboard,medicamentos,trabajadores,registrar_trabajadores,buscar_trabajador,usuarios2,eliminar_trabajador
from gestion import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('login/', index),
    path('dashboard/',login_required(dashboard)),

    path('medicamentos/',login_required(medicamentos)),

    path('trabajadores/',login_required(trabajadores)),

    path('buscar_trabajador/',login_required(buscar_trabajador)),

    
    path('eliminar_trabajador/',login_required(eliminar_trabajador)),

    path('registro_usuarios/',views.user_registro.as_view(), name="registro_usuarios"),

    path('usuarios/',views.user_list.as_view(), name="usuarios"),

    path('register_trabajador/',login_required(registrar_trabajadores)),

    path('',login_required(Inicio), name="index"),

    path('accounts/login/',LoginView.as_view(template_name='login.html'), name="login"),

    path('logout/',logout_then_login,name='logout'),

] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

