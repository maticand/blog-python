# Django
from django.shortcuts import render

# Utilidades
from django.utils import timezone

# Modelos
from .models import Post

# Errores
from django.shortcuts import render, get_object_or_404


def post_feed(request):
    posts = Post.objects.filter(fecha_publicado__lte=timezone.now()).order_by('fecha_publicado')
    return render(request, 'blog/post_feed.html', {'posts': posts})


def post_detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detalle.html', {'post': post})
