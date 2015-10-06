from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    fecha_nacimiento = models.DateField()
    
class Compra(models.Model):
    fecha_compra = models.DateField()
    precio = models.IntegerField()
    responsable = models.ForeignKey(Persona, related_name = 'responsable')
    compradores = models.ManyToManyField(Persona, related_name = 'compradores')
    lugar_compra = models.CharField

class Evento(models.Model):
    fecha_evento = models.DateField()
    compras = models.ManyToManyField(Compra)
    personas_invitadas = models.ManyToManyField(Persona)
    
class ComentarioCompra(models.Model):
    comentario = models.CharField(max_length = 200)
    autor = models.ForeignKey(Persona)
    
class PagoCompra(models.Model):
    compra = models.ForeignKey(Compra)
    persona = models.ForeignKey(Persona)
    fecha_pago = models.DateTimeField()
    
    
