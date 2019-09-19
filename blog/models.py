# Django
from django.db import models

# Utilidades
from django.utils import timezone


class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creado = models.DateTimeField(default=timezone.now)
    fecha_publicado = models.DateTimeField( blank=True, null=True)

    # Método Publicar
    def publicar(self):
        self.flecha_publicado = timezone.now()
        self.save()

    def  __str__(self):
        return self.titulo
