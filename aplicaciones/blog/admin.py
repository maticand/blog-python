from django.contrib import admin
from .models import Categoria
from .models import Autor
from .models import Post

# Third Party
# import-export resource
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria


class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor


class PostResource(resources.ModelResource):
    class Meta:
        model = Post


class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha_creacion',)
    list_filter = ('fecha_creacion',)
    resource_class = CategoriaResource


class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre','apellido','correo']
    list_display = ('nombre', 'apellido', 'correo', 'estado', 'fecha_creacion',)
    list_filter = ('nombre','apellido','correo','fecha_creacion',)
    resource_class = AutorResource


class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo','autor','categoria']
    list_display = ('titulo','autor','categoria', 'estado', 'fecha_creacion',)
    list_filter = ('titulo','autor','categoria','fecha_creacion',)
    resource_class = PostResource

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post, PostAdmin)
