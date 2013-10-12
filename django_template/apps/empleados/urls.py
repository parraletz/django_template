from django.conf.urls import url, patterns, include

urlpatterns = patterns('django_template.apps.empleados.views',
                      url(r'^e/index/$','listEmpleados_view'),
                      )
