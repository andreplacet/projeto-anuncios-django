from django.db import models


# Create your models here.

class Categoria(models.Model):
    titulo = models.fields.CharField(max_length=32)

    def __str__(self):
        return self.titulo


class Anuncio(models.Model):
    titulo = models.fields.CharField(max_length=40)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    made_in = models.DateTimeField(auto_now_add=True)
    changed_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
