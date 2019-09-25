# Django
from django.shortcuts import render
from .forms import PostForm
from django.shortcuts import redirect

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


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_publicado = timezone.now()
            post.save()
            return redirect('post_detalle', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_publicado = timezone.now()
            post.save()
            return redirect('post_detalle', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
