from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_feed, name='post_feed')
]
