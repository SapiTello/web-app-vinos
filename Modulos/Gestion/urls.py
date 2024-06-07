from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('productos/', views.productos, name='productos'),
    path('clientes/', views.clientes, name='clientes'),
    path('contacto/', views.contacto, name='contacto'),
]
