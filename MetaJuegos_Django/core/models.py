from django.db import models

# Create your models here.
class Credencial(models.Model):
    username = models.CharField(primary_key=True, max_length=60, verbose_name='Nombre Usuario')
    password = models.CharField(max_length=20, verbose_name='Contraseña Usuario')
    def __str__(self):
        return self.username
    

class Producto(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=16, verbose_name="Codigo_producto")
    nombre_producto = models.CharField(max_length=30, verbose_name="Nombre_producto")
    categoria = models.CharField(max_length=20, verbose_name="Categoria_producto")

    def __str__(self):
        return self.nombre_producto
    
class Carrito(models.Model):
    id_carrito = models.IntegerField(primary_key=True, verbose_name="Id_carrito")
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_carrito
    