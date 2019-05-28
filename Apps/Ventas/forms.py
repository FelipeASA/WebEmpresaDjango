from django import forms
from Apps.Ventas.models import *

class VentaProductoForm(forms.ModelForm):
    class Meta:
        model = VentaProducto

        fields=[
            'producto', 
            'cantidad',
        ]

        labels={
            'producto':'Producto : ',
            'cantidad':'Cantidad : ',
        }

        widgets={
            'producto':forms.Select(attrs={'class':'form-control'}),
            'cantidad':forms.TextInput(attrs={'class':'form-control'}),
        }


