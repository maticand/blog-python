from django.shortcuts import render
from .models import Post, Categoria
from django.shortcuts import get_object_or_404

# Q para la barra de busqueda
from django.db.models import Q

# Paginator para la paginacion
from django.core.paginator import Paginator

def index(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True).order_by('-fecha_publicado')
    if queryset:
        posts = Post.objects.filter(
        Q(titulo__icontains = queryset) |
        Q(descripcion__icontains = queryset)
        ).distinct()

    paginator = Paginator(posts, 1)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'index.html', {'posts': posts})


def sobremi(request):
    return render(request, 'blog/sobremi.html')


def contacto(request):
    return render(request, 'blog/contacto.html')


def seo(request):
    posts = Post.objects.filter(
    estado = True,
    categoria = Categoria.objects.get(nombre__iexact = 'seo')
    ).order_by('-fecha_publicado')

    paginator = Paginator(posts, 1)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/seo.html', {'posts': posts})


def detallePost(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'blog/post.html', {'detallePost': post})
