from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    fecha_nacimiento = models.DateField()
    #TODO ver como integrar con el usuario de django para mandar mail de notificaciones y permitir login

    def __str__(self):
        return self.nombre+' '+self.apellido

class Compra(models.Model):
    fecha_compra = models.DateField()
    precio = models.IntegerField()
    responsable = models.ForeignKey(Persona, related_name = 'responsable')
    compradores = models.ManyToManyField(Persona, related_name = 'compradores')
    lugar_compra = models.CharField
    #TODO agregar titulo y objeto a comprar

class Evento(models.Model):
    fecha_evento = models.DateField()
    compras = models.ManyToManyField(Compra)
    personas_invitadas = models.ManyToManyField(Persona)
    #TODO agregar titulo para el evento

class ComentarioCompra(models.Model):
    comentario = models.CharField(max_length = 200)
    autor = models.ForeignKey(Persona)

class PagoCompra(models.Model):
    compra = models.ForeignKey(Compra)
    persona = models.ForeignKey(Persona)
    fecha_pago = models.DateTimeField()
