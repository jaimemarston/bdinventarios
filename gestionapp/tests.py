from django.test import TestCase
from django.template.defaulttags import register
from django.utils.timezone import now
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from django.db.models import Sum
import xlwt
from gestionapp.models import (
    Deposito, Material, Articulo, Cliente, Proveedor, Unidad,
    Mcotizacion, Dcotizacion, Mmateriales, Dmateriales,
    Clientesdireccion, Banco, MaterialesEstado,
    CotizacionEstado)


from gestionapp.views import lista_stock
from gestionapp.views import procdic_detailprod
from gestionapp.views import articulos_detalle
from gestionapp.views import procdic_sumdetailprod

import time

t0 = time.time()
lista=lista_stock()
#lista=articulos_detalle()

#lista=procdic_detailprod('Articulo')
#print(lista['19TCV-091'][0])
#lista=procdic_sumdetailprod('Articulo')
t1 = time.time()
total = t1-t0

print ('Tiempo:',total)
#print (lista)