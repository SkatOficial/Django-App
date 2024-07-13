from django.db import models

class Marca(models.Model):
    id_marca    = models.AutoField(primary_key=True)
    nombre      = models.CharField(max_length=30 , null=False)
    
    def __str__(self):
        return str(self.nombre)

class Auto(models.Model):
    id_auto     = models.AutoField(primary_key=True)
    marca       = models.ForeignKey(Marca,on_delete = models.CASCADE)
    modelo      = models.CharField(max_length=30,null=False)
    año         = models.IntegerField()
    transmision = models.CharField(max_length=30)
    motor       = models.CharField(max_length=30)   
    img         = models.ImageField(upload_to='img/',null=False)
    velocidades = models.IntegerField()
    precio      = models.IntegerField(null=False)
    stock       = models.IntegerField(null=False)

    def __str__(self):
        return str(self.marca.nombre)+" "+str(self.modelo)
