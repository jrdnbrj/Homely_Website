from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    username = models.CharField(max_length = 50)
    mail = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

    def __str__(self):
        return "(" + str(self.id) + ") " + self.nombre

class Negocio(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    logo = models.CharField(max_length = 100)
    ubicacion = models.CharField(max_length = 100)

    def __str__(self):
        return "(" + str(self.id) + ") " + self.nombre

class Reseña(models.Model):
    id = models.AutoField(primary_key = True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    models.TextField(max_length = 200, default = "")
    calificacion = models.IntegerField()

    def __str__(self):
        return "(" + str(self.id) + ") " + str(self.fecha) + " - " + self.usuario

class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 100)
    foto = models.CharField(max_length = 100)
    descripcion = models.TextField(max_length = 200, default = "")
    numero_compras = models.IntegerField(default = 0, blank = True)
    precio = models.DecimalField(decimal_places = 4, max_digits = 7)
    reseñas = models.ManyToManyField(Reseña)

    def __str__(self):
        return "(" + str(self.id) + ") " + self.negocio

class Promocion(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    productos = models.ManyToManyField(Producto)
    foto = models.CharField(max_length = 100, null = True)
    descripcion = models.CharField(max_length = 100, null = True)
    precio = models.DecimalField(decimal_places = 4, max_digits = 7)

    def __str__(self):
        return "(" + str(self.id) + ") " + self.nombre

class Pedido(models.Model):
    id = models.AutoField(primary_key = True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default = "")
    fecha = models.DateTimeField()
    valor = models.DecimalField(decimal_places = 4, max_digits = 7)
    productos = models.ManyToManyField(Producto)
    promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE, null = True)
    direccion = models.CharField(max_length = 100, default = "")
    estado = models.BooleanField(default = False)

    def __str__(self):
        return "(" + str(self.id) + ") " + str(self.fecha) + " - " + self.usuario + " - " + str(self.valor)