class GaleriaAutos:        
    def __init__(self,request):
        self.request=request
        self.session=request.session
        self.galeria = self.session.get('galeriaAutos')
        if not self.galeria:
            self.galeria = self.session['galeriaAutos'] = {}
        
    def agregar(self,auto):
        if(str(auto.id_auto) not in self.galeria.keys()):
            self.galeria[auto.id_auto]={
                "id_auto": auto.id_auto,
                "marca": auto.marca.nombre,
                "modelo": auto.modelo,
                "año": auto.año,
                "transmision": auto.transmision,
                "motor": auto.motor,
                "img": auto.img.url,
                "velocidades": auto.velocidades,
                "precio": auto.precio,
                "stock": auto.stock,
            }
        self.guardarGaleria()

    def guardarGaleria(self):
        self.session["galeriaAutos"]=self.galeria
        self.session.modified=True
    
    def restarStock(self,auto):
        for key, value in self.galeria.items():
            if key==str(auto.id_auto):
                value["stock"]=value["stock"]-1
                break
        self.guardarGaleria()
    
    def sumarStock(self,auto):
        for key, value in self.galeria.items():
            if key==str(auto.id_auto):
                value["stock"]=value["stock"]+1
                break
        self.guardarGaleria()

    def estaVacia(self):
        return not bool(self.galeria)
    
    def tieneStock(self,auto):
        for key, value in self.galeria.items():
            if key==str(auto.id_auto):
                if(value["stock"]>0):
                    return True   
                return False
            
    def eliminar(self):
        del self.request.session['galeriaAutos']
        self.session.modified = True

    def getAutos(self):  
        galeria_aux = []
        for key, value in self.galeria.items():
            galeria_aux.append(value)
        return galeria_aux;   

    def getFiltroAutos(self, palabra):
        palabra = palabra.upper()
        galeria_aux = []
        for key, value in self.galeria.items():
            if(palabra in value["marca"].upper() or palabra in value["modelo"].upper()):
                galeria_aux.append(value)
        return galeria_aux;

    def getStockAuto(self, auto):
        for key, value in self.galeria.items():
            if key == str(auto.id_auto):
                return value["stock"]
        return False