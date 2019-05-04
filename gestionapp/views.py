from django.template.defaulttags import register
from django.utils.timezone import now
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from django.db.models import Sum
import xlwt

from gestionapp.models import (
    Deposito, Material, Articulo, Cliente, Proveedor, Unidad,
    Mcotizacion,Dcotizacion,Mmateriales,Dmateriales,
    Clientesdireccion, Banco, MaterialesEstado,
    CotizacionEstado)

from gestionapp.serializers import (
    DepositoSerializer, MaterialSerializer, ArticuloSerializer, ClienteSerializer, ProveedorSerializer, UnidadSerializer,
    McotizacionSerializer, DcotizacionSerializer,
    MmaterialesSerializer, DmaterialesSerializer,
    ClientesdireccionSerializer,
    ClientesdirecciondetalleSerializer, BancoSerializer,MaterialesEstadoSerializer,
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



# Create your views here.
from gestionapp.utils import render_to_pdf, PDFTemplateView, image_as_base64

@api_view(['GET', 'POST'])
def masivo_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class BancoList(generics.ListCreateAPIView):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer


class UnidadList(generics.ListCreateAPIView):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer


class UnidadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer


class DepositoList(generics.ListCreateAPIView):
    queryset = Deposito.objects.all()
    serializer_class = DepositoSerializer

class DepositoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deposito.objects.all()
    serializer_class = DepositoSerializer


class MaterialList(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class ArticuloList(generics.ListCreateAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer


class ArticuloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer


class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
    # bloquea permisos para usar token
    # permission_classes = (IsAuthenticated,)
    def perform_create(self, serializer):
        # guarda aud_idusu automatically en tabla.
        
        serializer.save(aud_idusu=self.request.user.username)

    

    # para filtrar datos
    """
    def get_queryset(self):
       
       # This view should return a list of all the purchases
       # for the currently authenticated user.
       
        # para otros filtros desde diccionario
        
        user = self.request.user.username
        return Cliente.objects.filter(aud_idusu=user)
    """


class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def perform_update(self, serializer):
        # guarda aud_idusu automatically en tabla.
        serializer.save(idioma='español',pais='Peru')

class ClienteListMasivo(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ProveedorList(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

    # para filtrar datos
    """
        # bloquea permisos para usar token
    # permission_classes = (IsAuthenticated,)
    def perform_create(self, serializer):
        # guarda aud_idusu automatically en tabla.
        serializer.save(aud_idusu=self.request.user.username)
        
    def get_queryset(self):
       
       # This view should return a list of all the purchases
       # for the currently authenticated user.
       
        # para otros filtros desde diccionario
        
        user = self.request.user.username
        return Cliente.objects.filter(aud_idusu=user)
    """


class ProveedorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class ProveedorListMasivo(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class McotizacionList(generics.ListCreateAPIView):
    queryset = Mcotizacion.objects.all()
    serializer_class = McotizacionSerializer
       

class McotizacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mcotizacion.objects.all()
    serializer_class = McotizacionSerializer
    

class DcotizacionList(generics.ListCreateAPIView):
    queryset = Dcotizacion.objects.all()
    serializer_class = DcotizacionSerializer

class DcotizacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dcotizacion.objects.all()
    serializer_class = DcotizacionSerializer
    
#
class MmaterialesList(generics.ListCreateAPIView):
    queryset = Mmateriales.objects.all()
    serializer_class = MmaterialesSerializer
       

class MmaterialesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mmateriales.objects.all()
    serializer_class = MmaterialesSerializer
    

class DmaterialesList(generics.ListCreateAPIView):
    queryset = Dmateriales.objects.all()
    serializer_class = DmaterialesSerializer

class DmaterialesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dmateriales.objects.all()
    serializer_class = DmaterialesSerializer


class Logout(APIView):
    queryset = User.objects.all()

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class ClientesDireccionlist(generics.ListCreateAPIView):
    queryset = Clientesdireccion.objects.all()
    serializer_class = ClientesdireccionSerializer


class ClientesDireccionlistdetail(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClientesdirecciondetalleSerializer


class CotizacionViewSet(viewsets.ModelViewSet):
    queryset = Mcotizacion.objects.all()
    serializer_class = McotizacionSerializer





class GeneratePDFCotizacionesMaster(PDFTemplateView):
    template_name = 'gestionapp/invoice.html'

    def get_context_data(self, **kwargs):
        maestro_cotizacion = Dcotizacion.objects.filter(master=1)

        return super(GeneratePDFCotizacionesMaster, self).get_context_data(
            pagesize='A4',
            title='Cotizacion Alitour',
            today=now(),
            cotizacion=maestro_cotizacion,
            **kwargs
        )


class GeneratePDFCotizacionesDetail(PDFTemplateView):
    template_name = 'gestionapp/invoice.html'

    def get_context_data(self, pk=None, *args, **kwargs):
        if pk is None:
            fields = ['Fecha', 'Hora', 'Descripcion', 'PAX', 'transporte', 'Total']
            fields_db = ['fechaini', 'horaini', 'descripcion', 'cantidad', 'desunimed', 'imptotal']
            headerset = Mcotizacion.objects.all().values()
            queryset = Mcotizacion.objects.all().values()
        else:
            fields = ['Fecha', 'Hora', 'Descripcion', 'PAX', 'Transporte', 'Total']
            fields_db = ['fechaini', 'horaini', 'descripcion', 'cantidad', 'desunimed', 'imptotal']
            headerset = Mcotizacion.objects.filter(id=pk).values()
            queryset = Dcotizacion.objects.filter(master=pk).values()
            rimptotal = 0 #list(Dcotizacion.objects.filter(master=pk).aggregate(Sum('imptotal')).values())[0] or 0
            imagenes = list(Dcotizacion.objects.filter(master=pk).values_list('desunimed')[0]) or ''
            #imagen_obt = list(Unidad.objects.filter(descripcion=imagenes).values_list())
            imagen_obt1 = list(Unidad.objects.values_list('foto1')[0])
            imagen_obt2 = list(Unidad.objects.values_list('foto2')[0])

        return super(GeneratePDFCotizacionesDetail, self).get_context_data(
            pagesize='A4',
            title='Cotizacion Alitour',
            today=now(),
            cotizacion=queryset,
            headerset=headerset,
            fields=fields,
            fields_db=fields_db,
            resultado_total=rimptotal,
            muestra_imagenes1=imagen_obt1,
            muestra_imagenes2=imagen_obt2,
            **kwargs
        )


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

class CotizacionEstadoViewSet(ModelViewSet):
    serializer_class = CotizacionEstadoSerializer
    queryset = CotizacionEstado.objects.all()

class CotizacionViewSet(viewsets.ModelViewSet):
    queryset = Mcotizacion.objects.all()
    serializer_class = McotizacionSerializer

#Materiales

class MaterialesEstadoViewSet(ModelViewSet):
    serializer_class = MaterialesEstadoSerializer
    queryset = MaterialesEstado.objects.all()

class MaterialesViewSet(viewsets.ModelViewSet):
    queryset = Mmateriales.objects.all()
    serializer_class = MmaterialesSerializer


class StockViewSet(viewsets.ModelViewSet):
   # queryset = Blogpost.objects.all().order_by('date')
    serializer_class = ArticuloSerializer

    def get_queryset(self):
        # Chances are, you're doing something more advanced here 
        # like filtering.
        Articulo.objects.all()
    #https://www.peterbe.com/plog/efficient-m2m-django-rest-framework
    def list(self, request, *args, **kwargs):
        #response = super().list(request, *args, **kwargs)
        #qs = self.get_queryset()
        
        category_names = {}
        for category in Articulo.objects.all():
            category_names[category.id] = category.descripcion

        usernames = [user.descripcion for user in Articulo.objects.all()]

        return Response(category_names)
               
        #return response



def xexport_users_xls(request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

def export_users_xls(request):
    nreport='materiales'
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename='+nreport+'.xls'
   
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(nreport)

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['CODIGO', 'DESCRIPCION', 'COLOR', 'UM', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Material.objects.all().values_list('codigo', 'descripcion', 'color', 'unimed')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response