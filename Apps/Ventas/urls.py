from django.conf.urls import url, include

from Apps.Ventas.views import *
# importamos de la app ventas

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^productos/', productos),
    url(r'^ventaf/', venta_view),
]
