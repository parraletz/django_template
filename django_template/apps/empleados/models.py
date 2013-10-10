from django.db import models

# Create your models here.

PUESTOS_CHOICES = (
    ('OP', 'Operador'),
    ('JD', 'Jefe de Departamento'),
    ('GE', 'Gerente'),
    ('SD','Subdirector'),
    ('DG', 'Director General'),
)


class Empleados(models.Model):
    nombre              = models.CharField(max_length=100)
    apellido_materno    = models.CharField(max_length=50)
    apellido_paterno    = models.CharField(max_length=50)
    edad                = models.IntegerField()
    puesto              = models.CharField(max_length=2, choices=PUESTOS_CHOICES)

    def __unicode__(self):
        nombreCompleto = "%s %s %s"%(self.nombre,self.apellido_materno,self.apellido_paterno)
        return nombreCompleto

    class Meta():
        verbose_name_plural = "Empleado"
