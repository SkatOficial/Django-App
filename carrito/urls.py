from django.urls import path
from . import views

urlpatterns = [
    path('',views.carrito, name ='carrito'),
    path('carrito/<int:id_auto>',views.agregar, name = 'agregar'),
    path("restar/<int:id_auto>/", views.restar_producto, name="restar")
]