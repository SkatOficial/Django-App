from django.urls import path
from . import views

urlpatterns = [
    path('',views.carrito, name ='carrito'),
    path('agregar/<int:id_auto>/', views.agregarProducto, name='agregar'),
    path("restar/<int:id_auto>/", views.restarProducto, name="restar"),
    path("pagar", views.pagar, name="pagar")
]