from django.shortcuts import render,redirect
from .carro import Carro
from autos.models import Auto

# Create your views here.
def carrito(request):
    return render(request,'carrito.html')

def agregar(request,id_auto):
    carro = Carro(request)

    auto=Auto.objects.get(id_auto=id_auto)
    print(auto.modelo)
    carro.agregar(auto=auto)
    
    return redirect(request.META.get('HTTP_REFERER'))

def restar_producto(request, id_auto):
    
    carro=Carro(request)
    
    auto=Auto.objects.get(id_auto=id_auto)
    
    carro.restar_auto(auto=auto)
    
    return redirect(request.META.get('HTTP_REFERER'))