from django.db import models

# Modelo para el accesorio
class accesorio(models.Model):
    tipo = models.CharField(max_length=50)  # Campo 'tipo' para el tipo de accesorio

# Modelo para el retiro
class retiro(models.Model):
    nombre = models.CharField(max_length=50)  # Campo para el nombre .
    apellidos = models.CharField(max_length=50)  # Campo  para los apellidos del retiro.
    num_id_pedido = models.CharField(max_length=12)  # Campo num_id_pedido para el número de identificación del pedido.
    email = models.EmailField()  # Campo 'email' para el correo electrónico del retiro.

# Modelo para el artículo
class articulo(models.Model):
    tipo_art = models.CharField(max_length=50)  # Campo para el tipo de artículo.
    talla = models.CharField(max_length=5)  # Campo  para la talla del .
    color = models.CharField(max_length=10)  # Color del artículo.
    fecha_llegada = models.DateField()  # Campo para la fecha de llegada del artículo.
    cantidad = models.IntegerField()  # Campo para la cantidad de artículos.
    retiro = models.ForeignKey(retiro, null=True, blank=True, on_delete=models.CASCADE)  # Relación ForeignKey con el modelo "retiro".
    accesorio = models.ManyToManyField(accesorio)  # Relación ManyToMany con el modelo "accesorio".
