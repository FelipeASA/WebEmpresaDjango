from django.conf.urls import url, include
from django.contrib import admin
# from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rrhh/', include('Apps.RRHH.urls')),
    url(r'^ventas/', include('Apps.Ventas.urls')),
]
