# Django
from django.shortcuts import render

# Utilidades
from django.utils import timezone

# Modelos
from .models import Post


def post_feed(request):
    posts = Post.objects.filter(fecha_publicado__lte=timezone.now()).order_by('fecha_publicado')
    return render(request, 'blog/post_feed.html', {'posts': posts})
