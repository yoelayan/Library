from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    biografia = models.TextField()

    def __str__(self):
        return self.nombre

    def contar_libros(self):
        return self.libro_set.count()

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    def publicado_ultimo_anio(self):
        return self.filter(fecha_publicacion__year=timezone.now().year - 1)
