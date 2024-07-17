class Carro:        
    def __init__(self,request):
        #del request.session['carro']
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
        print(self.carro)
        self.session["carro"]=self.carro
        self.session.modified=True
    
    def eliminar(self,auto):
        #primer ver si existe para poder eliminar
        if str(auto.id_auto) in self.carro:
            del self.carro[str(auto.id_auto)]
            self.guardar_carro()
  
    def restar_auto(self,auto):
        for key, value in self.carro.items():
            if key==str(auto.id_auto):
                value["cantidad"]=value["cantidad"]-1
                value["precioTotal"]=value["precioTotal"]-auto.precio
                if value["cantidad"]<1:
                   self.eliminar(auto) 
                break
        self.guardar_carro()

    def total_pago(self):
        total_a_pagar = 0
        for clave in self.carro:
            total_a_pagar += self.carro[clave]["precioTotal"]
        return total_a_pagar