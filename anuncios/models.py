from django.db import models


# Create your models here.

class Categoria(models.Model):
    titulo = models.fields.CharField(max_length=32)

    def __str__(self):
        return self.titulo