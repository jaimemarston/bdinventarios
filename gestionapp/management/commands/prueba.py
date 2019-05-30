
from django.core.management.base import BaseCommand
from django.test import TestCase
from django.template.defaulttags import register
from django.utils.timezone import now

from django.db.models import Sum
import xlwt
from models import (Mcotizacion, Dcotizacion, CotizacionEstado)

category_names = []
dic_masterprod = {} 
for master in Mcotizacion.objects.all():
    choices = {1: 'Inventario Inicial', 2: 'Ingreso Producto',3: 'Salida Producto',4: 'Anulado'}
    seltipo = choices.get(master.estado, 'default')
    dic_masterprod[master.id] = [master.estado, seltipo]
    #print(master.id,master.estado,seltipo)
    #referencia (dic_masterprod[15][1])
    #print (dic_masterprod[15][1])

print ('hellos')


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        pass