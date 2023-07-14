from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    # Otros campos del Autor

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    # Otros campos del Libro

    def __str__(self):
        return self.titulo
