from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    cantidad = models.IntegerField()


    def __str__(self) :
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.cantidad, self.precio)