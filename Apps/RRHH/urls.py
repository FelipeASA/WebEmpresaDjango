from django.conf.urls import url, include

from Apps.RRHH.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^about$', about),
]

# no usaremos path
# y junto con usar url definimos las rutas con expresiones regulares
# ^ inicio y $ para termino
# estos nombres index y about deben estar creados en views.py de la aplicacion
