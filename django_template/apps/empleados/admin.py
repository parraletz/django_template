from django.contrib import admin
from .models import Empleados

class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','apellido_paterno','apellido_materno','edad','puesto']
    search_fields = ('nombre',)
    list_filter = ('nombre',)
    #list_editable = ('nombre','apellido_paterno','apellido_materno','puesto',)

admin.site.register(Empleados,EmpleadosAdmin)
