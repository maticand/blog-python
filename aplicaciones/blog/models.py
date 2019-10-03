from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la Categoría', max_length=100, null=False, blank=False)
    estado = models.BooleanField('Activo/No Activo', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de Autor', max_length=100, null=False, blank=False)
    apellido = models.CharField('Apellido de Autor', max_length=100, null=False, blank=False)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    website = models.URLField('Website', null=True, blank=True)
    correo = models.EmailField('Correo Electrónico', null=False, blank=False)
    estado = models.BooleanField('Activo/No Activo', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0},{1}".format(self.apellido, self.nombre)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título', max_length=90, null=False, blank=False)
    slug = models.CharField('Slug', max_length=100, null=False, blank=False)
    descripcion = models.CharField('Descripción', max_length=110, null=False, blank=False)
    contenido = RichTextField()
    imagen = models.URLField('Imagen', max_length=255, null=False, blank=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo
