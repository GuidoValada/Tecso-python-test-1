from django.db import models
from technical.audit.models import Audit

class Titulares(Audit):
    cuit = models.CharField(max_length=50,blank=False,null=False,unique=True)
    tipo_titular = models.CharField(max_length=8,blank=False,null=False,verbose_name="Tipo de titular")
    nombre = models.CharField(max_length=80,blank=True,null=True)
    apellido = models.CharField(max_length=250,blank=True,null=True)
    dni = models.IntegerField(blank=True,null=True)
    razon_social = models.CharField(max_length=100,blank=True,null=True,verbose_name="Razon social")
    año_fundacion = models.CharField(max_length=4,blank=True,null=True, verbose_name="Año de fundacion")

    class Meta:
        verbose_name = 'Titular'
        verbose_name_plural = 'Titulares'

