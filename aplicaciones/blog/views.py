from django.shortcuts import render
from .models import Post, Categoria

def amp(request):
    return render(request,'index.amp.html')


def index(request):
    posts = Post.objects.filter(estado = True).order_by('fecha_publicado')
    return render(request,'index.html',{'posts':posts})


def sobremi(request):
    posts = Post.objects.filter(
    estado = True,
    categoria = Categoria.objects.get(nombre = 'seo'))
    return render(request,'blog/sobre-mi.html', {'posts':posts})


def about(request):
    return render(request,'blog/about.html')
