from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 50, unique=True)
    mail = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

    def __str__(self):
        return "(" + str(self.id) + ") " + self.username

class Negocio(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    logo = models.ImageField(upload_to='' ,max_length = None)
    ubicacion = models.CharField(max_length = 200)

    def __str__(self):
        return "(" + str(self.id) + ") " + self.nombre

class Reseña(models.Model):
    id = models.AutoField(primary_key = True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    texto = models.TextField(max_length = 1000, default = "")
    calificacion = models.IntegerField()

    def __str__(self):
        return "(" + str(self.id) + ") " + str(self.fecha) + " - " + str(self.usuario)

class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 100)
    foto = models.ImageField(upload_to='' ,max_length = 100, null=True)
    descripcion = models.TextField(max_length = 500, blank=True)
    numero_compras = models.IntegerField(default = 0, blank = True)
    precio = models.DecimalField(decimal_places = 2, max_digits = 5)
    reseñas = models.ManyToManyField(Reseña, related_name = "reseña", blank = True)

    def __str__(self):
        return "(" + str(self.id) + ") " + str(self.negocio) + " - " + self.nombre

class Promocion(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    productos = models.ManyToManyField(Producto)
    foto = models.ImageField(upload_to='' ,max_length = None, null = True)
    descripcion = models.TextField(max_length = 500, blank=True, default='')
    precio = models.DecimalField(decimal_places = 4, max_digits = 7)

    def __str__(self):
        return "(" + str(self.id) + ") " + self.nombre

class Pedido(models.Model):
    id = models.AutoField(primary_key = True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default = "")
    fecha = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(decimal_places = 4, max_digits = 7)
    productos = models.ManyToManyField(Producto)
    promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE, null = True)
    direccion = models.CharField(max_length = 100, default = "")
    estado = models.BooleanField(default = False)

    def __str__(self):
        return "(" + str(self.id) + ") " + str(self.fecha) + " - " + str(self.usuario) + " - " + str(self.valor)