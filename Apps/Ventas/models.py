from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre=models.CharField(max_length=100)
    precio=models.IntegerField()

    def NombreProducto(self):
        return self.nombre

    def __str__(self):
        return self.NombreProducto()

# Crear modelo para VentaProducto
class VentaProducto(models.Model):
    # atributos o propiedades
    producto=models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    fecha=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena= self.producto.nombre + " - " 
        cadena+= str(self.cantidad) +" - "
        cadena+= str(self.fecha)

        cadena = "Producto : {0} - Cantidad : {1} - Fecha : {2}"
        return cadena.format(self.producto.nombre, self.cantidad, self.fecha)
