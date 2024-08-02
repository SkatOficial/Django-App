from django.shortcuts import render, get_object_or_404
from .models import Auto
from .galeriaAutos import GaleriaAutos
# Create your views here.
def verAutos(request):
    galeria = GaleriaAutos(request)

    if galeria.estaVacia():#En caso de que "galeria" este vacia saca los datos de LA BDD
        autos = Auto.objects.all() 
        for auto in autos:
            galeria.agregar(auto=auto)

    context = {"autos" : galeria.getAutos()}
    return render(request,'verAutos.html',context)

def verAuto(request,id_auto):
    auto = get_object_or_404(Auto, id_auto=id_auto)
    context = {
        'auto': auto,
    }
    return render(request,'verAuto.html',context)

def buscarAutos(request):
    palabra_buscada = request.GET.get('buscador', '')
    galeria = GaleriaAutos(request)
    context = {
        'autos': galeria.getFiltroAutos(palabra_buscada),
    }
    return render(request,'verAutos.html',context)