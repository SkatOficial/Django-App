from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .carro import Carro
from autos.galeriaAutos import GaleriaAutos
from autos.models import Auto
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.
@login_required(login_url='signin')
def carrito(request):
    context = {"total_pagar" : Carro(request).totalPago()}
    return render(request,'carrito.html',context)

@login_required(login_url='signin')
def agregarProducto(request, id_auto):
    carro = Carro(request)
    galeria = GaleriaAutos(request)
    auto = Auto.objects.get(id_auto=id_auto)

    if galeria.tieneStock(auto=auto):
        carro.agregar(auto=auto)
        galeria.restarStock(auto=auto)
        stock_actualizado = galeria.getStockAuto(auto=auto)
        cantidad_carrito = carro.getCantidad(auto=auto)
        precio_total = carro.getPrecioTotal(auto=auto)
        precio_final = carro.totalPago()

        return JsonResponse({'status': 'success', 
                             'message': 'Auto agregado al carrito', 
                             'agregado' : True, 
                             'stockVehiculos': stock_actualizado,  
                             'cantidadCarrito': cantidad_carrito,
                             'precioTotal': precio_total,
                             'precioFinal': precio_final})


    return JsonResponse({'status': 'error', 
                         'message': 'Stock insuficiente'}, 
                         status=400)

@login_required(login_url='signin')
def restarProducto(request, id_auto):
    carro = Carro(request)
    galeria = GaleriaAutos(request)
    auto = Auto.objects.get(id_auto=id_auto)
    
    try:
        carro.restarAuto(auto=auto)
        galeria.sumarStock(auto=auto)
        stock_actualizado = galeria.getStockAuto(auto=auto)
        cantidad_carrito = carro.getCantidad(auto=auto)
        precio_total = carro.getPrecioTotal(auto=auto)
        precio_final = carro.totalPago()

        return JsonResponse({'status': 'success', 
                             'message': 'Auto Restado del carrito', 
                             'restado' : True, 
                             'stockVehiculos': stock_actualizado,  
                             'cantidadCarrito': cantidad_carrito,
                             'precioTotal': precio_total,
                             'precioFinal': precio_final})
    except ValueError:
        print("ERROR: ",ValueError)

@login_required(login_url='signin')
def pagar(request):

    carro=Carro(request)
    galeria = GaleriaAutos(request)
    
    for clave,value in carro.carro.items():
        auto = Auto.objects.get(id_auto=clave)
        auto.stock = auto.stock - value["cantidad"]
        auto.save()

    carro.eliminar()
    galeria.eliminar()
    
    return redirect(request.META.get('HTTP_REFERER'))