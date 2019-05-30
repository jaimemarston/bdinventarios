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

from gestionapp.serializers import (
    DepositoSerializer, MaterialSerializer, ArticuloSerializer, ClienteSerializer, ProveedorSerializer,
    UnidadSerializer,
    McotizacionSerializer, DcotizacionSerializer,
    MmaterialesSerializer, DmaterialesSerializer,
    ClientesdireccionSerializer,
    ClientesdirecciondetalleSerializer, BancoSerializer, MaterialesEstadoSerializer,
    CotizacionEstadoSerializer)

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import action
import base64
from django.templatetags.static import static
from django.http import HttpResponse
from gestionapp.utils import render_to_pdf, PDFTemplateView, image_as_base64

category_names = []
for category in Articulo.objects.all():
    data = {'codigo': category.codigo,
            'description': category.descripcion,
            'tipo': category.tipo,
            'genero': category.genero,
            'modelo': category.modelo,
            'talla': category.talla,
            'descolor': category.descolor,
            'desunimed': category.unimed,
            'precio': category.precioventa}
    category_names.append(data)

print (category_names)
