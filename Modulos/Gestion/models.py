from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Clientes(models.Model):
    IdCliente = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Correo = models.EmailField(max_length=50)
    Celular = models.CharField(max_length=9)

    def nombreClientes(self):
        txt = "{0}, {2}"
        return txt.format(self.Apellido,self.Nombre)
    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"

class Bodegas(models.Model):
    IdBodega = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=35)
    Ubicacion = models.CharField(max_length=35)
    Contacto = models.CharField(max_length=35)

class Vinos(models.Model):
    IdVino = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Tipo = models.CharField(max_length=35)
    Bodegas = models.ForeignKey(Bodegas,null=False,blank=False,on_delete=models.CASCADE)
    Año = models.CharField(max_length=35)
    Precio = models.DecimalField(max_digits=5,decimal_places=2)
    Stock = models.IntegerField()

class Venta(models.Model):
    IdVenta = models.AutoField(primary_key=True)
    Clientes = models.ForeignKey(Clientes,null=False, blank=False, on_delete=models.CASCADE)
    FechaPedido = models.DateField()
    Total = models.DecimalField(max_digits=5,decimal_places=2)

class DetalleVenta(models.Model):
    IdDetalleVenta = models.AutoField(primary_key=True)
    Venta = models.ForeignKey(Venta,null=False, blank=False, on_delete=models.CASCADE)
    Vinos = models.ForeignKey(Vinos, null=False, blank=False, on_delete=models.CASCADE)
    Cantidad = models.IntegerField()
    PrecioUnitario = models.DecimalField(max_digits=5,decimal_places=2)

class Proveedores(models.Model):
    IdProveedor = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=35)
    Ciudad = models.CharField(max_length=35)
    Celular = models.CharField(max_length=9)

    def __str__(self):
        return f"{self.Nombre}, ubicado en {self.Ciudad}"

class Pagos(models.Model):
    IdPagos = models.AutoField(primary_key=True)
    Venta = models.ForeignKey(Venta,null=False,blank=False,on_delete=models.CASCADE)
    MetodoPago = models.CharField(max_length=35)
    FechaPago = models.DateField()

class Administrador(models.Model):
    IdAdministrador = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=35)
    Apellido = models.CharField(max_length=35)
    Correo = models.EmailField(max_length=35)

class Compra(models.Model):
    IdCompra = models.AutoField(primary_key=True)
    Proveedores = models.ForeignKey(Proveedores,null=False,blank=False,on_delete=models.CASCADE)
    FechaCompra = models.DateField()
    Total = models.DecimalField(max_digits=5,decimal_places=2)

class DetalleCompra(models.Model):
    IdDetalleCompra = models.AutoField(primary_key=True)
    Compra = models.ForeignKey(Compra,null=False,blank=False,on_delete=models.CASCADE)
    Vinos = models.ForeignKey(Vinos,null=False,blank=False,on_delete=models.CASCADE)
    Cantidad = models.IntegerField()
    PrecioCompra = models.DecimalField(max_digits=5,decimal_places=2)















