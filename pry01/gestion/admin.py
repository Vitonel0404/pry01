from django.contrib import admin
from gestion.models import Trabajador
# Register your models here.

class TrabajadorAdmin(admin.ModelAdmin):
    list_display=("dni","nombre","apellido","email","telefono","direccion")
    search_fields=("dni","nombres","apellidos")





admin.site.register(Trabajador,TrabajadorAdmin)
