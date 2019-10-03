from django.contrib import admin
from .models import Categoria
from .models import Autor

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha_creacion',)
    list_filter = ('fecha_creacion',)

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombre','apellido','correo']
    list_display = ('nombre', 'apellido', 'correo', 'estado', 'fecha_creacion',)
    list_filter = ('nombre','apellido','correo','fecha_creacion',)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin) 
