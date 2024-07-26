from django.urls import path
from . import views

urlpatterns = [
    path('',views.carrito, name ='carrito'),
    path('agregar/<int:id_auto>',views.agregar, name = 'agregar'),
    path("restar/<int:id_auto>/", views.restar_producto, name="restar"),
    path("pagar", views.pagar, name="pagar")
]