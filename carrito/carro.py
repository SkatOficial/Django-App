class Carro:        
    def __init__(self,request):
        self.request=request
        self.session=request.session
        self.carro = self.session.get('carro')
        if not self.carro:
            self.carro = self.session['carro'] = {}
            
    def agregar(self,auto):
        if(str(auto.id_auto) not in self.carro.keys()):
            self.carro[auto.id_auto]={
                "id_auto":auto.id_auto,
                "marca":auto.marca.nombre, 
                "modelo":auto.modelo,
                "precio":auto.precio,
                "precioTotal":auto.precio,
                "cantidad":1,
                "imagen":auto.img.url
            }
        else:           
            for key, value in self.carro.items():
                if key==str(auto.id_auto):
                    value["cantidad"]= value["cantidad"]+1
                    value["precioTotal"]=value["precioTotal"]+auto.precio
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True
    
    def eliminar_auto(self,auto):
        #primer ver si existe para poder eliminar
        if str(auto.id_auto) in self.carro:
            del self.carro[str(auto.id_auto)]
            self.guardar_carro()
  
    def restarAuto(self,auto):
        for key, value in self.carro.items():
            if key==str(auto.id_auto):
                value["cantidad"]=value["cantidad"]-1
                value["precioTotal"]=value["precioTotal"]-auto.precio
                if value["cantidad"]<1:
                   self.eliminar_auto(auto) 
                break
        self.guardar_carro()

    def totalPago(self):
        total_a_pagar = 0
        for clave in self.carro:
            total_a_pagar += self.carro[clave]["precioTotal"]
        return total_a_pagar
    
    def eliminar(self):
        del self.request.session['carro']
        self.session.modified = True

    def getCantidad(self, auto):
        for key, value in self.carro.items():
            if key==str(auto.id_auto):
                return value["cantidad"]
        return 0

    def getPrecioTotal(self, auto):
        for key, value in self.carro.items():
            if key==str(auto.id_auto):
                return value["precioTotal"]
        return 0