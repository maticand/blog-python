from django.shortcuts import render
from .models import Post, Categoria

def index(request):
    posts = Post.objects.filter(estado = True).order_by('fecha_publicado')
    return render(request,'index.html',{'posts':posts})

def amp(request):
    return render(request,'index.amp.html')

def feed(request):
    return render(request,'feed.html')

def generales(request):
    posts = Post.objects.filter(
    estado = True,
    categoria = Categoria.objects.get(nombre = 'seo'))
    return render(request,'generales.html', {'posts':posts})
