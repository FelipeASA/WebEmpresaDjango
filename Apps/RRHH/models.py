from django.db import models
 
# Create your models here.
 
# modelo app RRHH
 
# definimos el modelo empleado 
# este modelo se creará como una tabla
# en la base de datos
class Empleado(models.Model):
    rut = models.CharField(max_length=8)
    dig = models.CharField(max_length=1)
    paterno = models.CharField(max_length=100)
    materno = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    SEXOS=(('F', 'Femenino'), ('M', 'Masculino'))
    Sexo=models.CharField(max_length=1, choices=SEXOS, default='M')
 
    # definimos el metodo NombreCompleto del empleado
    def NombreCompleto(self):
        cadena = self.nombres + " "
        cadena+= self.paterno + " " 
        cadena+= self.materno +" ("+ self.Sexo+") "
        return cadena
 
    # redifinimos el metodo __str__
    def __str__(self):  
        return self.NombreCompleto()
 
class Departamento(models.Model):
    nombre=models.CharField(max_length=50)
    areanegocio=models.CharField(max_length=50)
 
    def NombreDpto(self):
        return self.nombre + " - " + self.areanegocio
 
    def __str__(self):
        return self.NombreDpto()
 
class EmpleadoDpto(models.Model):
    Empleado=models.ForeignKey(Empleado, null=False, blank=False, on_delete=models.CASCADE)
    Departamento=models.ForeignKey(Departamento, null=False, blank=False, on_delete=models.CASCADE)
    Fecha=models.DateTimeField(auto_now_add=True)
 
    def Salida(self):
        return self.Empleado.NombreCompleto()+ " ==> " + self.Departamento.NombreDpto()
 
    def __str__(self):
        return self.Salida()
 