from django.db import models

class accesorio(models.Model):
    tipo = models.CharField(max_length=50)

class retiro(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    num_id_pedido = models.CharField(max_length=12)
    email = models.EmailField()

class articulo(models.Model):
    tipo_art = models.CharField(max_length=50)
    talla = models.CharField(max_length=5)
    color = models.CharField(max_length=10)
    fecha_llegada = models.DateField()
    cantidad = models.IntegerField()
    retiro = models.ForeignKey(retiro, null=True, blank=True, on_delete=models.CASCADE)
    accesorio = models.ManyToManyField(accesorio)
