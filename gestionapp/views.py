from django.template.defaulttags import register
from django.utils.timezone import now
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from django.db.models import Sum
import xlwt
import operator
import datetime



from gestionapp.models import (
    Deposito, Material, Articulo, Cliente, Proveedor, Unidad,
    Mcotizacion, Dcotizacion, Mmateriales, Dmateriales,
    Clientesdireccion, Banco, MaterialesEstado, Plaempleados, Plmovpersonal, Prorecetas, Prodetrecetas,
    Proproduccion, Prodetproduccion, CotizacionEstado, Pldatosreloj, Pltareosemanal,Plactacte)

from gestionapp.serializers import (
    DepositoSerializer, MaterialSerializer, ArticuloSerializer, ClienteSerializer, ProveedorSerializer,
    UnidadSerializer,
    McotizacionSerializer, DcotizacionSerializer,
    MmaterialesSerializer, DmaterialesSerializer,
    ClientesdireccionSerializer,
    ClientesdirecciondetalleSerializer, BancoSerializer, MaterialesEstadoSerializer,
    CotizacionEstadoSerializer,
    MempleadosSerializer,EmpleadoSerializer,PlmovpersonalSerializer,RecetasSerializer, ProddetrecetasSerializer, MrecetasSerializer,
    ProduccionSerializer, ProddetproduccionSerializer, MproduccionSerializer,
    PldatosrelojSerializer,PltareosemanalSerializer,MtareoSerializer,PlctacteSerializer)

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
from rest_framework.parsers import MultiPartParser
from procesar import cargar_data

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


class PldatosrelojViewSet(viewsets.ModelViewSet):
    queryset = Pldatosreloj.objects.all()
    serializer_class = PldatosrelojSerializer


class TareoViewSet(viewsets.ModelViewSet):
    queryset = Pltareosemanal.objects.all().order_by('codigo')
    serializer_class = MtareoSerializer


class PltareosemanalList(generics.ListCreateAPIView):
    queryset = Pltareosemanal.objects.all().order_by('codigo')
    serializer_class = PltareosemanalSerializer


class PldatosrelojList(generics.ListCreateAPIView):
    queryset = Pldatosreloj.objects.all().order_by('fechaini')
    serializer_class = PldatosrelojSerializer


class PldatosrelojDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pldatosreloj.objects.all().order_by('codigo')
    serializer_class = PldatosrelojSerializer

class DatosrelojUploadFile(APIView):
    parser_classes = (MultiPartParser,)
    #def post(self, request):
    def post(self, request, pk=None, *args, **kwargs):
        
        file = request.FILES['file']
        id_ = request.POST.get('idMasterReloj', None)
        print ('id_',id_, 'tamñ de archio', file.size)
        #file_data = file.read();
        cargar_data(file, int(id_))
        # Parse data
        return Response(status=204)

class GeneratePDFMaterialesDetail(PDFTemplateView):
    template_name = 'gestionapp/invoicemat.html'

   

#PRODUCCION

class ProduccionViewSet(viewsets.ModelViewSet):
    queryset = Proproduccion.objects.all().order_by('codigo')
    serializer_class = MproduccionSerializer

class ProduccionList(generics.ListCreateAPIView):
    queryset = Proproduccion.objects.all().order_by('codigo')
    serializer_class = ProduccionSerializer

class ProduccionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prodetproduccion.objects.all().order_by('codigo')
    serializer_class = ProddetproduccionSerializer

class ProdetproduccionList(generics.ListCreateAPIView):
    queryset = Prodetproduccion.objects.all().order_by('codigo')
    serializer_class = ProddetproduccionSerializer

class ProdetproduccionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prodetproduccion.objects.all().order_by('codigo')
    serializer_class = ProddetproduccionSerializer

#
class RecetasViewSet(viewsets.ModelViewSet):
    queryset = Prorecetas.objects.all().order_by('codigo')
    serializer_class = MrecetasSerializer

class RecetasList(generics.ListCreateAPIView):
    queryset = Prorecetas.objects.all().order_by('codigo')
    serializer_class = RecetasSerializer


class RecetasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prodetrecetas.objects.all().order_by('codigo')
    serializer_class = ProddetrecetasSerializer

class ProdetrecetasList(generics.ListCreateAPIView):
    queryset = Prodetrecetas.objects.all().order_by('codigo')
    serializer_class = ProddetrecetasSerializer


class ProdetrecetasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prodetrecetas.objects.all().order_by('codigo')
    serializer_class = ProddetrecetasSerializer


#Empleados
class EmpleadosViewSet(viewsets.ModelViewSet):
    queryset = Plaempleados.objects.all().order_by('codigo')
    serializer_class = MempleadosSerializer

class EmpleadoList(generics.ListCreateAPIView):
    queryset = Plaempleados.objects.all().order_by('codigo')
    serializer_class = EmpleadoSerializer


class EmpleadoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plaempleados.objects.all().order_by('codigo')
    serializer_class = EmpleadoSerializer

class PlmovpersonalList(generics.ListCreateAPIView):
    queryset = Plmovpersonal.objects.all().order_by('codigo')
    serializer_class = PlmovpersonalSerializer


class PlmovpersonalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plmovpersonal.objects.all().order_by('codigo')
    serializer_class = PlmovpersonalSerializer


class PlctacteList(generics.ListCreateAPIView):
    queryset = Plactacte.objects.all().order_by('codigo')
    serializer_class = PlctacteSerializer


class PlctacteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plactacte.objects.all().order_by('codigo')
    serializer_class = PlctacteSerializer

#INventarios


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
    permission_classes = (AllowAny,)

    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        print(self.request.query_params)
        return Articulo.objects.all()


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
        serializer.save(idioma='español', pais='Peru')


class ClienteListMasivo(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ProveedorList(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

    # para filtrar datos ultimo
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

    def get_queryset(self):
        print(self.request.query_params)
        return Mcotizacion.objects.all()


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
            fields = ['CODIGO', 'DESCRIPCION', 'MEDIDA', 'PRECIO', 'CANTIDAD', 'TOTAL']
            fields_db = ['codpro', 'descripcion', 'desunimed', 'precio', 'cantidad', 'imptotal']
            rimptotal = 'INVENTARIO INICIAL'
            headerset = Mcotizacion.objects.all().values()
            queryset = Mcotizacion.objects.all().values()
            imagen_obt1 = ''
            imagen_obt2 = ''
        else:
            fields = ['CODIGO', 'TIPO', 'GENERO', 'MODELO', 'TALLA', 'COLOR', 'MEDIDA', 'PRECIO', 'CANTIDAD', 'TOTAL']
            fields_db = ['codpro', 'tipo', 'genero', 'modelo', 'talla', 'descolor', 'desunimed', 'precio', 'cantidad',
                         'imptotal']

            fields_res = ['genero', 'cantidad__sum', 'imptotal__sum']
            headerset = Mcotizacion.objects.filter(id=pk).values()

            detail_total = Dcotizacion.objects.filter(master=pk).aggregate(Sum('imptotal'), Sum('cantidad'))

            queryset1 = Dcotizacion.objects.filter(master=pk).values().order_by('talla')
            nestado = list(Mcotizacion.objects.filter(id=pk).values_list('estado')[0])[0]
            resumenl = Dcotizacion.objects.filter(master=pk).values('genero').annotate(Sum('cantidad'), Sum('imptotal'))
            resumen = []
            for det in resumenl:
                data = {'genero': det['genero'],
                        'cantidad__sum': ("%.2f" % round(det['cantidad__sum'], 2)),
                        'imptotal__sum': ("%.2f" % round(det['imptotal__sum'], 2))}

                resumen.append(data)

            choices = {1: 'Inventario Inicial', 2: 'Ingreso Producto', 3: 'Salida Producto', 4: 'Anulado'}
            seltipo = choices.get(nestado, 'default')

            imagenes = list(Dcotizacion.objects.filter(master=pk).values_list('desunimed')[0]) or ''
            # imagen_obt = list(Unidad.objects.filter(descripcion=imagenes).values_list())

            category_names = []
            for det in queryset1:
                detail_cotizacion = list(
                    Articulo.objects.filter(codigo=det['codpro']).values_list('tipo', 'genero', 'modelo', 'talla',
                                                                              'descolor', 'unimed')[0])
                data = {'codpro': det['codpro'],
                        'descripcion': det['descripcion'],
                        'desunimed': detail_cotizacion[5],
                        'precio': det['precio'],
                        'tipo': detail_cotizacion[0],
                        'genero': detail_cotizacion[1],
                        'modelo': detail_cotizacion[2],
                        'talla': detail_cotizacion[3],
                        'descolor': detail_cotizacion[4],
                        'cantidad': det['cantidad'],
                        'imptotal': round(det['imptotal'], 2)}
                category_names.append(data)

            queryset = category_names

            imagen_obt1 = ''
            imagen_obt2 = ''

        return super(GeneratePDFCotizacionesDetail, self).get_context_data(
            pagesize='A4',
            title='Control de Productos',
            today=now(),
            cotizacion=queryset,
            headerset=headerset,
            fields=fields,
            fields_db=fields_db,
            fields_res=fields_res,
            tipo_movimiento=seltipo,
            resultado_total=("%.2f" % round(detail_total['imptotal__sum'], 2)),
            resultado_cantidad=("%.2f" % round(detail_total['cantidad__sum'], 2)),
            muestra_imagenes1=imagen_obt1,
            muestra_imagenes2=imagen_obt2,
            resumen_detalle=resumen,

            **kwargs
        )


class GeneratePDFMaterialesDetail(PDFTemplateView):
    template_name = 'gestionapp/invoicemat.html'

    def get_context_data(self, pk=None, *args, **kwargs):
        if pk is None:
            fields = ['CODIGO', 'DESCRIPCION', 'MEDIDA', 'PRECIO', 'CANTIDAD', 'TOTAL']
            fields_db = ['codpro', 'descripcion', 'desunimed', 'precio', 'cantidad', 'imptotal']
            rimptotal = 'INVENTARIO INICIAL'
            headerset = Mmateriales.objects.all().values()
            queryset = Mmateriales.objects.all().values()
            imagen_obt1 = ''
            imagen_obt2 = ''
        else:
            fields = ['CODIGO', 'TIPO', 'COLOR', 'MEDIDA', 'PRECIO', 'CANTIDAD', 'TOTAL']
            fields_db = ['codpro', 'tipo', 'descolor', 'desunimed', 'precio', 'cantidad', 'imptotal']

            fields_res = ['tipo', 'cantidad__sum', 'imptotal__sum']
            headerset = Mmateriales.objects.filter(id=pk).values()

            detail_total = Dmateriales.objects.filter(master=pk).aggregate(Sum('imptotal'), Sum('cantidad'))

            queryset1 = Dmateriales.objects.filter(master=pk).values().order_by('talla')
            nestado = list(Mmateriales.objects.filter(id=pk).values_list('estado')[0])[0]
            resumen = Dmateriales.objects.filter(master=pk).values('tipo').annotate(Sum('cantidad'), Sum('imptotal'))

            choices = {1: 'Inventario Inicial', 2: 'Ingreso Producto', 3: 'Salida Producto', 4: 'Anulado'}
            seltipo = choices.get(nestado, 'default')

            imagenes = list(Dmateriales.objects.filter(master=pk).values_list('desunimed')[0]) or ''
            # imagen_obt = list(Unidad.objects.filter(descripcion=imagenes).values_list())

            category_names = []
            for det in queryset1:
                detail_cotizacion = list(
                    Material.objects.filter(codigo=det['codpro']).values_list('tipo', 'genero', 'modelo', 'talla',
                                                                              'descolor')[0])
                data = {'codpro': det['codpro'],
                        'descripcion': det['descripcion'],
                        'desunimed': det['desunimed'],
                        'precio': det['precio'],
                        'tipo': detail_cotizacion[0],
                        'genero': detail_cotizacion[1],
                        'modelo': detail_cotizacion[2],
                        'talla': detail_cotizacion[3],
                        'descolor': detail_cotizacion[4],
                        'cantidad': det['cantidad'],
                        'imptotal': det['imptotal']}
                category_names.append(data)

            queryset = category_names

            imagen_obt1 = ''
            imagen_obt2 = ''

        return super(GeneratePDFMaterialesDetail, self).get_context_data(
            pagesize='A4',
            title='Control de Materiales',
            today=now(),
            cotizacion=queryset,
            headerset=headerset,
            fields=fields,
            fields_db=fields_db,
            fields_res=fields_res,
            tipo_movimiento=seltipo,
            resultado_total=("%.2f" % round(detail_total['imptotal__sum'], 2)),
            resultado_cantidad=("%.2f" % round(detail_total['cantidad__sum'], 2)),
            muestra_imagenes1=imagen_obt1,
            muestra_imagenes2=imagen_obt2,
            resumen_detalle=resumen,

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

    def get_queryset(self):
        month = self.request.query_params.get('month', None)
        if month:
            month = int(month) + 1
            return Mcotizacion.objects.filter(fechadoc__month=month).order_by('codigo')
        return Mcotizacion.objects.order_by('codigo')


class ListViewParam(generics.ListCreateAPIView):
    queryset = Mcotizacion.objects.all()
    serializer_class = McotizacionSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('from', None)
        end_date = self.request.query_params.get('end', None)

        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        if start_date and end_date:
            return Mcotizacion.objects.filter(fechadoc__range=(start_date, end_date))
        else:
            return Mcotizacion.objects.all()


# Materiales

class MaterialesEstadoViewSet(ModelViewSet):
    serializer_class = MaterialesEstadoSerializer
    queryset = MaterialesEstado.objects.all()


class MaterialesViewSet(viewsets.ModelViewSet):
    queryset = Mmateriales.objects.all()
    serializer_class = MmaterialesSerializer

    def get_queryset(self):
        month = self.request.query_params.get('month', None)
        if month:
            month = int(month) + 1
            return Mmateriales.objects.filter(fechadoc__month=month).order_by('codigo')
        return Mmateriales.objects.order_by('codigo')



class lista_articulos_detalleViewSet(viewsets.ModelViewSet):
    # queryset = Blogpost.objects.all().order_by('date')
    serializer_class = ArticuloSerializer

    def get_queryset(self):
        # Chances are, you're doing something more advanced here 
        # like filtering.
        Articulo.objects.all()

    # https://www.peterbe.com/plog/efficient-m2m-django-rest-framework
    def list(self, request, *args, **kwargs):
        # response = super().list(request, *args, **kwargs)
        # qs = self.get_queryset()
        category_names = articulos_detalle()
        return Response(category_names)


class control_pagosViewSet(viewsets.ModelViewSet):
    # queryset = Blogpost.objects.all().order_by('date')
    serializer_class = ProveedorSerializer

    def get_queryset(self):
        # Chances are, you're doing something more advanced here 
        # like filtering.
        Proveedor.objects.all()

    # https://www.peterbe.com/plog/efficient-m2m-django-rest-framework
    def list(self, request, *args, **kwargs):
        # response = super().list(request, *args, **kwargs)
        # qs = self.get_queryset()

        category_names = control_pagos()
        return Response(category_names)


class lista_materiales_detalleViewSet(viewsets.ModelViewSet):
    # queryset = Blogpost.objects.all().order_by('date')
    serializer_class = MaterialSerializer

    def get_queryset(self):
        # Chances are, you're doing something more advanced here 
        # like filtering.
        Material.objects.all()

    # https://www.peterbe.com/plog/efficient-m2m-django-rest-framework
    def list(self, request, *args, **kwargs):
        # response = super().list(request, *args, **kwargs)
        # qs = self.get_queryset()

        category_names = []

        for category in Material.objects.all():
            xinvini = 0
            xingresos = 0
            xsalidas = 0
            xsaldo = 0
            datail = []
            for estado in Mmateriales.objects.all():
                nestado = estado.estado
                pkmaster = estado.id
                choices = {1: 'Inventario Inicial', 2: 'Ingreso Producto', 3: 'Salida Producto', 4: 'Anulado'}
                seltipo = choices.get(nestado, 'default')
                detail_material = Dmateriales.objects.filter(codpro=category.codigo, master=pkmaster).aggregate(
                    Sum('cantidad'))

                valor_cantidad = detail_material['cantidad__sum'] if type(detail_material['cantidad__sum']) != type(
                    None) else 0

                invini = valor_cantidad if nestado == 1 else 0
                ingresos = valor_cantidad if nestado == 2 else 0
                salidas = valor_cantidad if nestado == 3 else 0

                xinvini += invini
                xingresos += ingresos
                xsalidas += salidas

                for det in Dmateriales.objects.filter(codpro=category.codigo, master=pkmaster):
                    datodet = {
                        "id": 7,
                        "codigo": det.codigo,
                        "descripcion": seltipo,
                        "cantidad": det.cantidad,
                        "precio": det.precio,
                        "imptotal": det.imptotal,
                    }
                    datail.append(datodet)
            xsaldo = (xinvini + xingresos) - xsalidas
            # print (category.codigo,valor_cantidad,nestado,xinvini,xingresos,xsalidas)
            data = {'codigo': category.codigo,
                    'descripcion': category.descripcion,
                    'inv.inicial': xinvini,
                    'ingresos': xingresos,
                    'salidas': xsalidas,
                    'saldo.actual': xsaldo,
                    "cotizaciones": datail}

            category_names.append(data)
        return Response(category_names)


class listaarticuloViewSet(viewsets.ModelViewSet):
    # queryset = Blogpost.objects.all().order_by('date')
    serializer_class = ArticuloSerializer
    paginate_by = 10
    paginate_by_param = 'page_size'
    max_paginate_by = 10

    def get_queryset(self):
        # Chances are, you're doing something more advanced here 
        # like filtering.
        category_names = []
        # Articulo.objects.all()

    # https://www.peterbe.com/plog/efficient-m2m-django-rest-framework
    def list(self, request, *args, **kwargs):
        # response = super().list(request, *args, **kwargs)
        # qs = self.get_queryset()

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
        paginate_by = 10
        paginate_by_param = 'page_size'
        max_paginate_by = 100
        return Response(category_names)


class alerta_stock_prod_ViewSet(viewsets.ModelViewSet):
    # queryset = Blogpost.objects.all().order_by('date')
    serializer_class = ArticuloSerializer

    def get_queryset(self):
        # Chances are, you're doing something more advanced here
        # like filtering.
        Articulo.objects.all()

    # https://www.peterbe.com/plog/efficient-m2m-django-rest-framework
    def list(self, request, *args, **kwargs):
        # response = super().list(request, *args, **kwargs)
        # qs = self.get_queryset()
        # choices = {1: 'Inventario Inicial', 2: 'Ingreso Producto',3: 'Salida Producto',4: 'Anulado'}
        start_date = self.request.query_params.get('from', None)
        end_date = self.request.query_params.get('end', None)

        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        print(start_date, end_date)
        # if start_date and end_date:
        #     return Mcotizacion.objects.filter(fechadoc__range=(start_date, end_date))
        # else:
        #     return Mcotizacion.objects.all()
        
        category_names = lista_stock('cantidad',start_date, end_date,True)

        return Response(category_names)

class alerta_stock_mat_ViewSet(viewsets.ModelViewSet):
    # queryset = Blogpost.objects.all().order_by('date')
    serializer_class = MaterialSerializer

    def get_queryset(self):
        # Chances are, you're doing something more advanced here
        # like filtering.
        Material.objects.all()

    # https://www.peterbe.com/plog/efficient-m2m-django-rest-framework
    def list(self, request, *args, **kwargs):
        # response = super().list(request, *args, **kwargs)
        # qs = self.get_queryset()
        # choices = {1: 'Inventario Inicial', 2: 'Ingreso Producto',3: 'Salida Producto',4: 'Anulado'}
        start_date = self.request.query_params.get('from', None)
        end_date = self.request.query_params.get('end', None)

        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        print(start_date, end_date)
        # if start_date and end_date:
        #     return Mcotizacion.objects.filter(fechadoc__range=(start_date, end_date))
        # else:
        #     return Mcotizacion.objects.all()
        
        category_names = lista_stock_mat('cantidad',start_date, end_date,True)

        return Response(category_names)


class calculaplanillaViewSet(viewsets.ModelViewSet):
    # queryset = Blogpost.objects.all().order_by('date')
    serializer_class = EmpleadoSerializer

    def get_queryset(self):
        # Chances are, you're doing something more advanced here 
        # like filtering.
        Plaempleados.objects.all()

    # https://www.peterbe.com/plog/efficient-m2m-django-rest-framework
    def list(self, request):
        # response = super().list(request, *args, **kwargs)
        # qs = self.get_queryset()
        print('id->', request.GET.get('master_id', 0))
        #plctacte ingresos gastos
        #plmovpersonal sueldo 
        xmaster = int(request.GET.get('master_id', 0))

        semana = Pltareosemanal.objects.filter(id=xmaster)
        days_ES = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

        category_names = []
        for category in Plaempleados.objects.all():
            sueldos = Plmovpersonal.objects.filter(codemp=category.codigo)
            
            if sueldos:
               
                cturno = sueldos[0].turno if sueldos[0].turno else ''
                nimporte = sueldos[0].importe if sueldos[0].importe else 0.00
                nimpdia1=nimpdia2=nimpdia3=nimpdia4=nimpdia5=nimpdia6=nimpdia7=0
                detallesemana = Pldatosreloj.objects.filter(master=xmaster,codigo=category.codigo).order_by('fechaini')
                for det in detallesemana:
                    #if det.fechaini:
                    fecha = det.fechaini
                    #print('det.fechaini',type(fecha))
                    #now = datetime.datetime.strptime(fecha, '%Y-%m-%d')
                    cdia=fecha.strftime("{%w}").format(*days_ES)
                    ndia=int(fecha.strftime("%w"))
                    
                    nhrsdia1 = det.hrtotal
                    ntime = datetime.datetime.strptime(nhrsdia1,'%H:%M')
                    
                    if ntime.hour>8:
                       print('ndiaultimo',type(ndia),cdia,fecha,nimporte,type(ntime.hour))    
                       nimpdia1 = nimporte if ndia==1 else nimpdia1
                       nimpdia2 = nimporte if ndia==2 else nimpdia2
                       nimpdia3 = nimporte if ndia==3 else nimpdia3
                       nimpdia4 = nimporte if ndia==4 else nimpdia4
                       nimpdia5 = round((nimporte/2),2) if ndia==5 else nimpdia5
                       nimpdia6 = nimporte if ndia==6 else nimpdia6
                       nimpdia7 = nimporte if ndia==7 else nimpdia7
                       
                    

                #print ('ndia',category.codigo,nimpdia4)
                    # "fechaini": "2019-07-29",
                    # "fechafin": "2019-07-29",
                    # "hrentrada": "07:54",
                    # "hrinidesc": "13:02",
                    # "hrfindesc": "13:58",
                    # "hrsalida": "19:42", 
                ntotal = nimpdia1+nimpdia2+nimpdia3+nimpdia4+nimpdia5+nimpdia6+nimpdia7
                data = {'codigo': category.codigo,
                        'nombre': category.nombre,
                        'turno': cturno,
                        'sueldo':nimporte,
                        'hrsextras': 00,
                        'dia1': nimpdia1,
                        'dia2': nimpdia2,
                        'dia3': nimpdia3,
                        'dia4': nimpdia4,
                        'dia5': nimpdia5,
                        'dia6': nimpdia6,
                        'dia7': nimpdia7,
                        'total': ntotal}
                #nimpdia1=0
                category_names.append(data)

        return Response(category_names)

        # return response


class listamaterialViewSet(viewsets.ModelViewSet):
    # queryset = Blogpost.objects.all().order_by('date')
    serializer_class = MaterialSerializer

    def get_queryset(self):
        # Chances are, you're doing something more advanced here 
        # like filtering.
        Material.objects.all()

    # https://www.peterbe.com/plog/efficient-m2m-django-rest-framework
    def list(self, request, *args, **kwargs):
        # response = super().list(request, *args, **kwargs)
        # qs = self.get_queryset()

        category_names = []
        for category in Material.objects.all():
            data = {'codigo': category.codigo,
                    'description': category.descripcion}
            category_names.append(data)

        return Response(category_names)

        # return response


class StockViewSet(viewsets.ModelViewSet):
    # queryset = Blogpost.objects.all().order_by('date')
    serializer_class = ArticuloSerializer

    def get_queryset(self):
        # Chances are, you're doing something more advanced here
        # like filtering.
        Articulo.objects.all()

    # https://www.peterbe.com/plog/efficient-m2m-django-rest-framework
    def list(self, request, *args, **kwargs):
        # response = super().list(request, *args, **kwargs)
        # qs = self.get_queryset()
        # choices = {1: 'Inventario Inicial', 2: 'Ingreso Producto',3: 'Salida Producto',4: 'Anulado'}
        start_date = self.request.query_params.get('from', None)
        end_date = self.request.query_params.get('end', None)

        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        print(start_date, end_date)
        # if start_date and end_date:
        #     return Mcotizacion.objects.filter(fechadoc__range=(start_date, end_date))
        # else:
        #     return Mcotizacion.objects.all()

        category_names = lista_stock('talla',start_date, end_date)

        return Response(category_names)

        # return response


class Stock_matViewSet(viewsets.ModelViewSet):
    # queryset = Blogpost.objects.all().order_by('date')
    serializer_class = MaterialSerializer

    def get_queryset(self):
        # Chances are, you're doing something more advanced here 
        # like filtering.
        Material.objects.all()

    # https://www.peterbe.com/plog/efficient-m2m-django-rest-framework
    def list(self, request, *args, **kwargs):
        # response = super().list(request, *args, **kwargs)
        # qs = self.get_queryset()
        # choices = {1: 'Inventario Inicial', 2: 'Ingreso Producto',3: 'Salida Producto',4: 'Anulado'}
        start_date = self.request.query_params.get('from', None)
        end_date = self.request.query_params.get('end', None)

        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        print(start_date, end_date)
        # if start_date and end_date:
        #     return Mcotizacion.objects.filter(fechadoc__range=(start_date, end_date))
        # else:
        #     return Mcotizacion.objects.all()

        category_names = lista_stock_mat('talla',start_date, end_date)
        return Response(category_names)

        # return response


def export_xls_arti(request):
    nreport = 'productos'
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=' + nreport + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(nreport)

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['CODIGO', 'DESCRIPCION', 'COLOR', 'TIPO', 'TALLA', 'UM', 'PRECIOVENTA']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Articulo.objects.all().values_list('codigo', 'descripcion', 'descolor', 'tipo', 'talla', 'unimed',
                                              'precioventa')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def export_users_xls(request):
    nreport = 'materiales'
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=' + nreport + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(nreport)

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['CODIGO', 'DESCRIPCION', 'COLOR', 'TIPO', 'UM', 'PRECIOVENTA']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Material.objects.all().values_list('codigo', 'descripcion', 'descolor', 'tipo', 'unimed', 'precioventa')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


# DETALLE DE MATERIALES A EXCEL
def export_xls_matdetalle(request):
    nreport = 'Detalle_Materiales'
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=' + nreport + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(nreport)
    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    category_names = materiales_detalle()

    columns = ['CODIGO', 'DESCRIPCION', 'INVINICIAL', 'INGRESOS', 'SALIDAS', 'SALDOACTUAL']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # add_sheet is used to create sheet. 
    for row in category_names:
        row_num += 1
        # print(row_num,col_num,row[col_num],font_style)
        ws.write(row_num, 0, row['codigo'], font_style)
        ws.write(row_num, 1, row['descripcion'], font_style)
        ws.write(row_num, 2, row['inv.inicial'], font_style)
        ws.write(row_num, 3, row['ingresos'], font_style)
        ws.write(row_num, 4, row['salidas'], font_style)
        ws.write(row_num, 5, row['saldo.actual'], font_style)
        for detalle in row['materiales']:
            row_num += 1
            ws.write(row_num, 0, detalle['codigo'], font_style)
            ws.write(row_num, 1, detalle['descripcion'], font_style)
            ws.write(row_num, 3, detalle['precio'], font_style)
            ws.write(row_num, 4, detalle['imptotal'], font_style)
            ws.write(row_num, 5, detalle['cantidad'], font_style)
    wb.save(response)
    return response


# DETALLE DE PAGO PROVEEDORES

def export_xls_control_pagos(request):
    nreport = 'Detalle_Pago'
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=' + nreport + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(nreport)

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    category_names = control_pagos()
    columns = ['CODIGO', 'DESCRIPCION', 'INVINICIAL', 'INGRESOS', 'SALIDAS', 'SALDOACTUAL', 'COBRADO', 'PAGADO',
               'SALDO']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # add_sheet is used to create sheet. 
    for row in category_names:
        row_num += 1
        # print(row_num,col_num,row[col_num],font_style)
        ws.write(row_num, 0, row['codigo'], font_style)
        ws.write(row_num, 1, row['descripcion'], font_style)
        ws.write(row_num, 2, row['inv.inicial'], font_style)
        ws.write(row_num, 3, row['ingresos'], font_style)
        ws.write(row_num, 4, row['salidas'], font_style)
        ws.write(row_num, 5, row['saldo.actual'], font_style)
        ws.write(row_num, 6, row['importecobrado'], font_style)
        ws.write(row_num, 7, row['importepagado'], font_style)
        ws.write(row_num, 8, row['saldo_importe'], font_style)
        for detalle in row['cotizaciones']:
            row_num += 1
            ws.write(row_num, 0, detalle['codigo'], font_style)
            ws.write(row_num, 1, detalle['descripcion'], font_style)
            ws.write(row_num, 2, detalle['precio'], font_style)
            ws.write(row_num, 3, detalle['imptotal'], font_style)
            ws.write(row_num, 4, detalle['cantidad'], font_style)
    wb.save(response)
    return response


# DETALLE DE PRODUCTOS A EXCEL
def export_xls_proddetalle(request):
    nreport = 'Detalle_productos'
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=' + nreport + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(nreport)

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    category_names = articulos_detalle()

    columns = ['CODIGO', 'DESCRIPCION', 'INVINICIAL', 'INGRESOS', 'SALIDAS', 'SALDOACTUAL']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # add_sheet is used to create sheet. 
    for row in category_names:
        row_num += 1
        # print(row_num,col_num,row[col_num],font_style)
        ws.write(row_num, 0, row['codigo'], font_style)
        ws.write(row_num, 1, row['descripcion'], font_style)
        ws.write(row_num, 2, row['inv.inicial'], font_style)
        ws.write(row_num, 3, row['ingresos'], font_style)
        ws.write(row_num, 4, row['salidas'], font_style)
        ws.write(row_num, 5, row['saldo.actual'], font_style)
        for detalle in row['cotizaciones']:
            row_num += 1
            ws.write(row_num, 0, detalle['codigo'], font_style)
            ws.write(row_num, 1, detalle['descripcion'], font_style)
            ws.write(row_num, 2, detalle['cantidad'], font_style)
            ws.write(row_num, 3, detalle['precio'], font_style)
            ws.write(row_num, 4, detalle['imptotal'], font_style)

    wb.save(response)
    return response


def export_xls_stock_mat(request):
    nreport = 'stock_materiales'
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=' + nreport + '.xls'

    # Workbook is created
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(nreport)

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    category_names = lista_stock_mat()

    columns = ['CODIGO', 'DESCRIPCION', 'INVINICIAL', 'INGRESOS', 'SALIDAS', 'SALDOACTUAL']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # add_sheet is used to create sheet. 
    for row in category_names:
        row_num += 1
        # print(row_num,col_num,row[col_num],font_style)
        ws.write(row_num, 0, row['codigo'], font_style)
        ws.write(row_num, 1, row['descripcion'], font_style)
        ws.write(row_num, 2, row['inv.inicial'], font_style)
        ws.write(row_num, 3, row['ingresos'], font_style)
        ws.write(row_num, 4, row['salidas'], font_style)
        ws.write(row_num, 5, row['saldo.actual'], font_style)

        # ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def export_xls_stock(request):
    nreport = 'stock_productos'
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=' + nreport + '.xls'

    # Workbook is created
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(nreport)

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    category_names = lista_stock()

    columns = ['CODIGO', 'DESCRIPCION', 'TIPO', 'GENERO', 'MODELO', 'TALLA', 'DESCOLOR', 'DESUNIMED', 'INVINICIAL',
               'INGRESOS', 'SALIDAS', 'SALDOACTUAL']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # add_sheet is used to create sheet. 
    for row in category_names:
        row_num += 1
        # print(row_num,col_num,row[col_num],font_style)
        ws.write(row_num, 0, row['codigo'], font_style)
        ws.write(row_num, 1, row['descripcion'], font_style)
        ws.write(row_num, 2, row['tipo'], font_style)
        ws.write(row_num, 3, row['genero'], font_style)
        ws.write(row_num, 4, row['modelo'], font_style)
        ws.write(row_num, 5, row['talla'], font_style)
        ws.write(row_num, 6, row['descolor'], font_style)
        ws.write(row_num, 7, row['desunimed'], font_style)
        ws.write(row_num, 8, row['inv.inicial'], font_style)
        ws.write(row_num, 9, row['ingresos'], font_style)
        ws.write(row_num, 10, row['salidas'], font_style)
        ws.write(row_num, 11, row['saldo.actual'], font_style)

        # ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def export_xls_alerta_stock_prod(request):
    nreport = 'alerta_stock_prod'
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=' + nreport + '.xls'
    
    # Workbook is created
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(nreport)

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    category_names = lista_stock('cantidad',None, None,True)



    columns = ['CODIGO', 'DESCRIPCION', 'TIPO', 'GENERO', 'MODELO', 'TALLA', 'DESCOLOR', 'DESUNIMED', 'SALDOACTUAL' ,'STOCKMIN' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # add_sheet is used to create sheet. 
    for row in category_names:
        row_num += 1
        # print(row_num,col_num,row[col_num],font_style)
        ws.write(row_num, 0, row['codigo'], font_style)
        ws.write(row_num, 1, row['descripcion'], font_style)
        ws.write(row_num, 2, row['tipo'], font_style)
        ws.write(row_num, 3, row['genero'], font_style)
        ws.write(row_num, 4, row['modelo'], font_style)
        ws.write(row_num, 5, row['talla'], font_style)
        ws.write(row_num, 6, row['descolor'], font_style)
        ws.write(row_num, 7, row['desunimed'], font_style)
        ws.write(row_num, 8, row['saldo.actual'], font_style)
        ws.write(row_num, 9, row['stockmin'], font_style)


        # ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_xls_alerta_stock_mat(request):
    nreport = 'alerta_stock_mat'
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=' + nreport + '.xls'
    
    # Workbook is created
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(nreport)

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    category_names = lista_stock_mat('cantidad',None, None,True)



    columns = ['CODIGO', 'DESCRIPCION', 'SALDOACTUAL' ,'STOCKMIN' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # add_sheet is used to create sheet. 
    for row in category_names:
        row_num += 1
        # print(row_num,col_num,row[col_num],font_style)
        ws.write(row_num, 0, row['codigo'], font_style)
        ws.write(row_num, 1, row['descripcion'], font_style)
        ws.write(row_num, 2, row['saldo.actual'], font_style)
        ws.write(row_num, 3, row['stockmin'], font_style)


        # ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response



def lista_stock(order=None, startdate=None, enddate=None, sistockmin=False):
    category_names = []
    dic_sumdetailprod = procdic_sumdetailprod('Articulo','Dcotizacion')

    for category in Articulo.objects.all().order_by('talla'):
        xinvini = 0
        xingresos = 0
        xsalidas = 0
        xsaldo = 0
        if startdate and enddate:
            queryset = Mcotizacion.objects.filter(fechadoc__range=(startdate, enddate))
        else:
            queryset = Mcotizacion.objects.all()
        for estado in queryset:
            nestado = estado.estado
            # pkmaster = estado.id
            pkmaster = str(estado.id) + category.codigo
            # detail_cotizacion = Dcotizacion.objects.filter(codpro=category.codigo,master=pkmaster).aggregate(Sum('cantidad'))
            # valor_cantidad = detail_cotizacion['cantidad__sum'] if  type(detail_cotizacion['cantidad__sum'])   != type(None) else 0

            valor_cantidad = 0

            if pkmaster in dic_sumdetailprod:
                valor_cantidad = sum(dic_sumdetailprod[pkmaster][1]) if type(dic_sumdetailprod[pkmaster][1]) != type(
                    None) else 0

            invini = valor_cantidad if nestado == 1 else 0
            ingresos = valor_cantidad if nestado == 2 else 0
            salidas = valor_cantidad if nestado == 3 else 0

            xinvini += invini
            xingresos += ingresos
            xsalidas += salidas
        xsaldo = (xinvini + xingresos) - xsalidas
        # print (category.codigo,valor_cantidad,nestado,xinvini,xingresos,xsalidas)
        data = {'codigo': category.codigo,
                'descripcion': category.descripcion,
                'tipo': category.tipo,
                'genero': category.genero,
                'modelo': category.modelo,
                'talla': category.talla,
                'descolor': category.descolor,
                'desunimed': category.unimed,
                'inv.inicial': xinvini,
                'ingresos': xingresos,
                'salidas': xsalidas,
                'saldo.actual': xsaldo,
                'stockmin': category.stockmin,
                }

        category_names.append(data)
    
    if not sistockmin:
        for foo in category_names:
            del foo['stockmin']
    elif sistockmin:
        nitem=0
        for foo in category_names:
            del foo['inv.inicial']
            del foo['ingresos']
            del foo['salidas']
        category_names = [key for key in category_names if float(key['saldo.actual'])>=float(0) and float(key['stockmin'])>float(0) ]
        category_names = [key for key in category_names if float(key['stockmin'])>=float(key['saldo.actual'])]
    
    return category_names


def lista_stock_mat(order=None, startdate=None, enddate=None, sistockmin=False):
    category_names = []
    dic_sumdetailprod = procdic_sumdetailprod('Material','Dmateriales')

    for category in Material.objects.all():
        xinvini = 0
        xingresos = 0
        xsalidas = 0
        xsaldo = 0
        if startdate and enddate:
            queryset = Mmateriales.objects.filter(fechadoc__range=(startdate, enddate))
        else:
            queryset = Mmateriales.objects.all()
        for estado in queryset:
            nestado = estado.estado
            pkmaster = str(estado.id) + category.codigo
            valor_cantidad = 0
            if pkmaster in dic_sumdetailprod:
                valor_cantidad = sum(dic_sumdetailprod[pkmaster][1]) if type(dic_sumdetailprod[pkmaster][1]) != type(
                    None) else 0

            invini = valor_cantidad if nestado == 1 else 0
            ingresos = valor_cantidad if nestado == 2 else 0
            salidas = valor_cantidad if nestado == 3 else 0

            xinvini += invini
            xingresos += ingresos
            xsalidas += salidas
        xsaldo = (xinvini + xingresos) - xsalidas
        # print (category.codigo,valor_cantidad,nestado,xinvini,xingresos,xsalidas)
        data = {'codigo': category.codigo,
                'descripcion': category.descripcion,
                'inv.inicial': xinvini,
                'ingresos': xingresos,
                'salidas': xsalidas,
                'saldo.actual': xsaldo,
                'stockmin': category.stockmin,
                }

        category_names.append(data)
    if not sistockmin:
        for foo in category_names:
            del foo['stockmin']
    elif sistockmin:
        nitem=0
        for foo in category_names:
            del foo['inv.inicial']
            del foo['ingresos']
            del foo['salidas']
        category_names = [key for key in category_names if float(key['saldo.actual'])>float(0) and float(key['stockmin'])>float(0) ]
        category_names = [key for key in category_names if float(key['stockmin'])>=float(key['saldo.actual'])]
    
    return category_names


def articulos_detalle():
    category_names = []
    dic_sumdetailprod = procdic_sumdetailprod('Articulo','Dcotizacion')
    dic_detailprod = procdic_detailprod('Articulo','Dcotizacion')

    for category in Articulo.objects.all().order_by('talla'):
        xinvini = 0
        xingresos = 0
        xsalidas = 0
        xsaldo = 0
        datail = []
        for estado in Mcotizacion.objects.all():
            nestado = estado.estado
            choices = {1: 'Inventario Inicial', 2: 'Ingreso Producto', 3: 'Salida Producto', 4: 'Anulado'}
            seltipo = choices.get(nestado, 'default')
            pkmaster = str(estado.id) + category.codigo
            valor_cantidad = 0

            if pkmaster in dic_sumdetailprod:
                valor_cantidad = sum(dic_sumdetailprod[pkmaster][1]) if type(dic_sumdetailprod[pkmaster][1]) != type(
                    None) else 0
            invini = valor_cantidad if nestado == 1 else 0
            ingresos = valor_cantidad if nestado == 2 else 0
            salidas = valor_cantidad if nestado == 3 else 0

            xinvini += invini
            xingresos += ingresos
            xsalidas += salidas
            if pkmaster in dic_detailprod:
                datodet = {
                    "id": 7,
                    "codigo": dic_detailprod[pkmaster][0],
                    "descripcion": seltipo,
                    "cantidad": dic_detailprod[pkmaster][3],
                    "precio": dic_detailprod[pkmaster][4],
                    "imptotal": dic_detailprod[pkmaster][5],
                }
                datail.append(datodet)

        xsaldo = (xinvini + xingresos) - xsalidas
        data = {'codigo': category.codigo,
                'descripcion': category.descripcion,
                'unimed': category.unimed,
                'talla': category.talla,
                'inv.inicial': xinvini,
                'ingresos': xingresos,
                'salidas': xsalidas,
                'saldo.actual': xsaldo,
                "cotizaciones": datail}
        category_names.append(data)
    return category_names


def materiales_detalle():
    category_names = []
    dic_sumdetailprod = procdic_sumdetailprod('Material','Dmateriales')
    dic_detailprod = procdic_detailprod('Material','Dmateriales')

    for category in Material.objects.all():
        xinvini = 0
        xingresos = 0
        xsalidas = 0
        xsaldo = 0
        datail = []
        for estado in Mmateriales.objects.all():
            nestado = estado.estado
            pkmaster = str(estado.id) + category.codigo
            choices = {1: 'Inventario Inicial', 2: 'Ingreso Producto', 3: 'Salida Producto', 4: 'Anulado'}
            seltipo = choices.get(nestado, 'default')
            
            valor_cantidad = 0
            if pkmaster in dic_sumdetailprod:
                valor_cantidad = sum(dic_sumdetailprod[pkmaster][1]) if type(dic_sumdetailprod[pkmaster][1]) != type(
                    None) else 0

            invini = valor_cantidad if nestado == 1 else 0
            ingresos = valor_cantidad if nestado == 2 else 0
            salidas = valor_cantidad if nestado == 3 else 0

            xinvini += invini
            xingresos += ingresos
            xsalidas += salidas

            for det in dic_detailprod:
                datodet = {
                    "id": 7,
                    "codigo": dic_detailprod[pkmaster][0],
                    "descripcion": seltipo,
                    "cantidad": dic_detailprod[pkmaster][3],
                    "precio": dic_detailprod[pkmaster][4],
                    "imptotal": dic_detailprod[pkmaster][5],
                }
                datail.append(datodet)

        xsaldo = (xinvini + xingresos) - xsalidas
        
        data = {'codigo': category.codigo,
                'descripcion': category.descripcion,
                'unimed': category.unimed,
                'inv.inicial': xinvini,
                'ingresos': xingresos,
                'salidas': xsalidas,
                'saldo.actual': xsaldo,
                "materiales": datail}

        category_names.append(data)

    return category_names


def control_pagos():
    category_names = []
    for category in Proveedor.objects.all():
        xinvini = 0
        xingresos = 0
        xsalidas = 0
        xsaldo = 0
        nimppagado = 0
        nimpcobrado = 0
        xnimpcobrado = 0
        xnimppagado = 0
        datail = []
        xtipogrupo= "P" if category.grupo == "PROVEEDOR" else "C"
        for estado in Mcotizacion.objects.filter(ruc=category.ruc):
            nestado = estado.estado
            pkmaster = estado.id
            
            nimppagado = estado.imppagado if estado.imppagado else 0
            if category.ruc == '000001':
                   print  ('Movi Pagado',pkmaster,nimppagado)
            xnimppagado += nimppagado 
            choices = {1: 'Inventario Inicial', 2: 'Ingreso Producto', 3: 'Salida Producto', 4: 'Anulado'}
            seltipo = choices.get(nestado, 'default')
            detail_material = Dcotizacion.objects.filter(master=pkmaster).aggregate(Sum('cantidad'))

            nimpcobrado_det = Dcotizacion.objects.filter(master=pkmaster).aggregate(Sum('imptotal'))
            if category.ruc == '000001':
               print  ('Movi Cobrado',pkmaster,nimpcobrado_det)

            nimpcobrado = nimpcobrado_det['imptotal__sum'] if type(nimpcobrado_det['imptotal__sum']) != type(
                None) else 0
            valor_cantidad = detail_material['cantidad__sum'] if type(detail_material['cantidad__sum']) != type(
                None) else 0

            invini = valor_cantidad if nestado == 1 else 0
            ingresos = valor_cantidad if nestado == 2 else 0
            salidas = valor_cantidad if nestado == 3 else 0

            xnimpcobrado += nimpcobrado
            xinvini += invini
            xingresos += ingresos
            xsalidas += salidas

            for det in Dcotizacion.objects.filter(master=pkmaster):
                datodet = {
                    "id": 7,
                    "codigo": "PS-" +str(det.codigo) if nestado==3 else "PI-"+str(det.codigo),
                    "tipo": seltipo,
                    "codpro": det.codpro,
                    "descripcion": det.descripcion,
                    "cantidad": det.cantidad,
                    "precio": det.precio,
                    "imptotal": det.imptotal,
                }

                datail.append(datodet)

        xsaldo = (xinvini + xingresos) - xsalidas

        # MATERIALES
        for estado in Mmateriales.objects.filter(ruc=category.ruc):
            nestado = estado.estado
            pkmaster = estado.id
            nimppagado = estado.imppagado if estado.imppagado else 0
            # if category.ruc == '000001':
            #        print  ('Movi Pagado',pkmaster,nimppagado)
            xnimppagado += nimppagado 
            choices = {1: 'Inventario Inicial', 2: 'Ingreso Producto', 3: 'Salida Producto', 4: 'Anulado'}
            seltipo = choices.get(nestado, 'default')
            detail_material = Dmateriales.objects.filter(master=pkmaster).aggregate(Sum('cantidad'))

            nimpcobrado_det = Dmateriales.objects.filter(master=pkmaster).aggregate(Sum('imptotal'))
            # if category.ruc == '000001':
            #    print  ('Movi Cobrado',pkmaster,nimpcobrado_det)

            nimpcobrado = nimpcobrado_det['imptotal__sum'] if type(nimpcobrado_det['imptotal__sum']) != type(
                None) else 0
            valor_cantidad = detail_material['cantidad__sum'] if type(detail_material['cantidad__sum']) != type(
                None) else 0

            invini = valor_cantidad if nestado == 1 else 0
            ingresos = valor_cantidad if nestado == 2 else 0
            salidas = valor_cantidad if nestado == 3 else 0

            xnimpcobrado += nimpcobrado
            xinvini += invini
            xingresos += ingresos
            xsalidas += salidas

            for det in Dmateriales.objects.filter(master=pkmaster):
                datodet = {
                    "id": 7,
                    "codigo": "MS-" +str(det.codigo) if nestado==3 else "MI-"+str(det.codigo),
                    "tipo": seltipo,
                    "codpro": det.codpro,
                    "descripcion": det.descripcion,
                    "cantidad": det.cantidad,
                    "precio": det.precio,
                    "imptotal": det.imptotal,
                }

                datail.append(datodet)


        # print (category.codigo,valor_cantidad,nestado,xinvini,xingresos,xsalidas)
        data = {'codigo': category.ruc,
                'descripcion': category.nombre,
                'inv.inicial': xinvini,
                'ingresos': xingresos,
                'salidas': xsalidas,
                'saldo.actual': xsaldo,
                'importecobrado': xnimpcobrado,
                'importepagado': xnimppagado,
                'saldo_importe': xnimpcobrado-xnimppagado if xtipogrupo == "C" else xnimppagado-xnimpcobrado ,
                "cotizaciones": datail}

        category_names.append(data)

    return category_names


# def procdic_masterprod():
#     dic_masterprod = {}
#     for master in Mcotizacion.objects.all():
#         choices = {1: 'Inventario Inicial', 2: 'Ingreso Producto', 3: 'Salida Producto', 4: 'Anulado'}
#         seltipo = choices.get(master.estado, 'default')
#         dic_masterprod[master.id] = [master.estado, seltipo]

#     return dic_masterprod

def procdic_sumdetailprod(tbase,tdetalle):
    #tbase =Articulos
    #tdetalle =Dcotizacion o mcotizacion
    dic_sumdetailprod = {}
    for category in eval(tbase).objects.all():
        for resdet in eval(tdetalle).objects.filter(codpro=category.codigo).values('master', 'codpro').annotate(
                Sum('cantidad')):
            key = str(resdet['master']) + resdet['codpro']
            dic_sumdetailprod[key] = [resdet['codpro'], [round(resdet['cantidad__sum'], 2)]]
    return dic_sumdetailprod


def procdic_detailprod(tbase,tdetalle):
      #tbase =Articulos
      #tdetalle =Dcotizacion
    dic_detailprod = {}
    for category in eval(tbase).objects.all():
        for resdet in eval(tdetalle).objects.filter(codpro=category.codigo).values():
            key = str(resdet['codigo']) + resdet['codpro']
            dic_detailprod[key] = [str(resdet['codigo']), resdet['codpro'], resdet['descripcion'], resdet['cantidad'],
                                   resdet['precio'], resdet['imptotal']]
    return dic_detailprod


