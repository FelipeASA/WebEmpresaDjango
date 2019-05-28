from django.contrib import admin

# importamos todos los modelos de la 
# aplicacion RRHH
from Apps.RRHH.models import *

# Register your models here.

# registramos el modelo
admin.site.register(Empleado)
# modelos agregados
admin.site.register(Departamento)
admin.site.register(EmpleadoDpto)

# con estas definiciones estamos diciendo 
# que el modulo admin de nuestro proyecto 
# pueda administrar los modelos de nuestra app RRHH
