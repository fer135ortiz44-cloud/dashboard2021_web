from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    # Foto panorámica de la sede (Punto 10)
    foto = models.ImageField(upload_to='sucursales/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.ciudad}"

class MetodoPago(models.Model):
    nombre = models.CharField(max_length=100)
    # Estatus requerido en el Punto 11
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    correo = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    # Estatus requerido en el Punto 8
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

class Vendedor(models.Model):
    nombre = models.CharField(max_length=150)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    correo = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    # Identificación visual automática requerida en el Punto 9
    foto = models.ImageField(upload_to='vendedores/', blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    stock = models.IntegerField(default=0)
    # Estatus requerido en el Punto 7
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"