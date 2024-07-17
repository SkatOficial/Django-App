from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .carro import Carro
from autos.galeriaAutos import GaleriaAutos
from autos.models import Auto


# Create your views here.
@login_required(login_url='signin')
def carrito(request):
    context = {"total_pagar" : Carro(request).total_pago()}
    return render(request,'carrito.html',context)

@login_required(login_url='signin')
def agregar(request,id_auto):
    carro = Carro(request)
    galeria = GaleriaAutos(request)

    auto=Auto.objects.get(id_auto=id_auto)

    if(galeria.tiene_stock(auto=auto)):
        carro.agregar(auto=auto)
        galeria.restar_stock(auto=auto)
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='signin')
def restar_producto(request, id_auto):
    
    carro=Carro(request)
    galeria=GaleriaAutos(request)

    auto=Auto.objects.get(id_auto=id_auto)

    carro.restar_auto(auto=auto)
    galeria.sumar_stock(auto=auto)
    
    return redirect(request.META.get('HTTP_REFERER'))

