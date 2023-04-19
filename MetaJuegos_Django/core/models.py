from django.db import models

# Create your models here.
class Credencial(models.Model):
    idUsuario = models.IntegerField(primary_key=True, verbose_name='Id de Usuario')
    nombreUsuario = models.CharField(max_length=60, verbose_name='Nombre de Usuario')

    def __str__(self):
        return self.nombreUsuario
    
class Usuario(models.Model):
    nombreCompleto = models.CharField(primary_key=True, max_length=60, verbose_name="Nombre Completo Usuario")
    correo = models.CharField(max_length=60, verbose_name="Correo Usuario")
    numeroTelefono = models.IntegerField(verbose_name="Numero Usuario")
    Credencial = models.ForeignKey(Credencial, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreCompleto
    
class Producto(models.Model):
    idProducto = models.CharField(primary_key=True, max_length=60, verbose_name="Id Producto")
    nombreProducto = models.CharField(max_length=60, verbose_name="Nombre Producto")
    categoria = models.IntegerField(verbose_name="Categoria")

    def __str__(self):
        return self.idProducto
    
class Carrito(models.Model):
    idCarrito = models.IntegerField(primary_key=True, verbose_name="Id Carrito")
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.idCarrito
    