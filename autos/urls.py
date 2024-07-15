from django.urls import path
from . import views

urlpatterns = [
    path('',views.verAutos, name = 'verAutos'),
    path('verAuto/<int:id_auto>',views.verAuto, name = 'verAuto'),
    path('filtro/<str:palabra_buscada>',views.buscarAutos, name = 'buscarAutos')
]