# Django
from django.db import models
from tinymce import HTMLField
from django.template.defaultfilters import slugify
from django.utils import timezone


class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = HTMLField('texto')
    slug = models.SlugField()
    fecha_creado = models.DateTimeField(default=timezone.now)
    fecha_publicado = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
            super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo
