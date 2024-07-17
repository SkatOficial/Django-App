from django.shortcuts import render, get_object_or_404
from .models import Auto
from .galeriaAutos import GaleriaAutos
from django.db.models import Q
# Create your views here.
def verAutos(request):
    galeria = GaleriaAutos(request)

    if galeria.esta_vacia():#En caso de que "galeria" este vacia saca los datos de LA BDD
        autos = Auto.objects.all() 
        for auto in autos:
            galeria.agregar(auto=auto)

    return render(request,'verAutos.html')

def verAuto(request,id_auto):
    auto = get_object_or_404(Auto, id_auto=id_auto)
    context = {
        'auto': auto,
    }
    return render(request,'verAuto.html',context)

def buscarAutos(request):
    palabra_buscada = request.GET.get('palabra_buscada', '')
    autos = Auto.objects.filter(Q(modelo__contains=palabra_buscada) | Q(marca__nombre__contains=palabra_buscada)).distinct()# 'Q' sirve para crear consultas complejas, en este caso quiero combinar 2 consultas y eliminar duplicados (.distinct())
    context = {
        'autos': autos,
    }
    return render(request,'verAutos.html',context)