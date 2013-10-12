from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import Empleados

def listEmpleados_view(request):
    lista = Empleados.objects.all()
    data = {'lista':lista}
    return render_to_response('empleados/listaEmpleados.html',data,context_instance=RequestContext(request))
