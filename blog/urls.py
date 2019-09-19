# Django
from django.urls import path

# Vistas
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.post_feed, name='post_feed'),
]
