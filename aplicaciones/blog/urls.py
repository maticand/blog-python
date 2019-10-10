from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('sobremi', views.sobremi, name='sobremi'),
    path('contacto', views.contacto, name='contacto'),
    path('seo', views.seo, name='seo'),
    path('django', views.django, name='django'),
    path('<slug:slug>', views.detallePost, name='detallePost'),


    # path('post/<int:pk>/', views.post_detalle, name='post_detalle'),
    # path('post/new', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]
