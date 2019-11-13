from django.urls import path

from . import views

# URL Definition

urlpatterns = [
    path('', views.index, name='index'),
]