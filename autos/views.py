from django.shortcuts import render, get_object_or_404
from .models import Auto
from django.db.models import Q
# Create your views here.
def verAutos(request):
    autos = Auto.objects.all() 
    context = {
        'autos': autos,
    }
    return render(request,'verAutos.html',context)

def verAuto(request,id_auto):
    auto = get_object_or_404(Auto, id_auto=id_auto)
    context = {
        'auto': auto,
    }
    return render(request,'verAuto.html',context)

def buscarAutos(request, palabra_buscada):
    autos = Auto.objects.filter(Q(modelo__contains=palabra_buscada) | Q(marca__nombre__contains=palabra_buscada)).distinct()
    context = {
        'autos': autos,
    }
    return render(request,'verAutos.html',context)