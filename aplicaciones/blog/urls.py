from django.urls import path
from . import views


urlpatterns = [
    path('amp', views.amp, name='amp'),
    path('', views.index, name='index'),
    path('feed', views.feed, name='feed'),
    # path('post/<int:pk>/', views.post_detalle, name='post_detalle'),
    # path('post/new', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]
