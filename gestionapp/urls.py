from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'mcotizacion', views.CotizacionViewSet)
router.register(r'mmateriales', views.MaterialesViewSet)
router.register(r'cotizacion_estado', views.CotizacionEstadoViewSet)

#Productos
router.register(r'lista_stock', views.StockViewSet, base_name='put-something-here', )
router.register(r'lista_articulos', views.listaarticuloViewSet, base_name='put-something-here', )
router.register(r'lista_articulos_detalle', views.lista_articulos_detalleViewSet, base_name='put-something-here', )

#Materiales
router.register(r'lista_stock_mat', views.Stock_matViewSet, base_name='put-something-here', )
router.register(r'lista_materiales', views.listamaterialViewSet, base_name='put-something-here', )
router.register(r'lista_materiales_detalle', views.lista_materiales_detalleViewSet, base_name='put-something-here', )

#Proveedores
router.register(r'control_pagos', views.control_pagosViewSet, base_name='put-something-here', )


     


urlpatterns = [
    url(r'^deposito$', views.DepositoList.as_view()),
    url(r'^deposito/(?P<pk>[0-9]+)$', views.DepositoDetail.as_view()),

    url(r'^articulo$', views.ArticuloList.as_view()),
    url(r'^articulo/(?P<pk>[0-9]+)$', views.ArticuloDetail.as_view()),

    url(r'^material$', views.MaterialList.as_view()),
    url(r'^material/(?P<pk>[0-9]+)$', views.MaterialDetail.as_view()),

    url(r'^cliente$', views.ClienteList.as_view()),
    url(r'^cliente/(?P<pk>[0-9]+)$', views.ClienteDetail.as_view()),
    url(r'^clientemasivo$', views.masivo_list),

    url(r'^proveedor$', views.ProveedorList.as_view()),
    url(r'^proveedor/(?P<pk>[0-9]+)$', views.ProveedorDetail.as_view()),

    url(r'^unidad$', views.UnidadList.as_view()),
    url(r'^unidad/(?P<pk>[0-9]+)$', views.UnidadDetail.as_view()),
    # url(r'^mcotizacion$', views.CotizacionViewSet.as_view()),
    # url(r'^mcotizacion/(?P<pk>[0-9]+)$', views.CotizacionViewSet.as_view()),
    url(r'^dcotizacion$', views.DcotizacionList.as_view()),
    url(r'^dcotizacion/(?P<pk>[0-9]+)$', views.DcotizacionDetail.as_view()),

    url(r'^dmateriales$', views.DmaterialesList.as_view()),
    url(r'^dmateriales/(?P<pk>[0-9]+)$', views.DmaterialesDetail.as_view()),

    url(r'^clientesdireccion$', views.ClientesDireccionlist.as_view()),
    url(r'^clientesdirecciondetail$', views.ClientesDireccionlistdetail.as_view()),
    url(r'^', include(router.urls)),

    url(r'^banco$', views.BancoList.as_view()),
    url(r'^generate_pdf$', views.GeneratePDFCotizacionesDetail.as_view()),
    url(r'^generate_pdf/(?P<pk>\d+)/$', views.GeneratePDFCotizacionesDetail.as_view()),
    url(r'^generatemat_pdf/(?P<pk>\d+)/$', views.GeneratePDFMaterialesDetail.as_view()),

    
    #http://localhost:8080/filtro/2019-05-13/2019-05-13/
    url(r'^filtro/(?P<sk>[\w\-\.]+)/(?P<ek>[\w\-\.]+)/$', views.ListViewParam.as_view()),
    #url(r'^filtro/(?P<pk>[\w\-\.]+)/(?P<sk>[\w\-\.]+)/(?P<ek>[\w\-\.]+)/$', views.ListViewParam.as_view()),
    #url(r'^filtro$', views.ListViewParam.as_view()),
    url(r'^generate_html$', TemplateView.as_view(template_name="gestionapp/invoice.html")),
    
    #1 Lista productos
    url(r'^export_xls_arti$', views.export_xls_arti, name='productos'),
    #1.3 Kardex DETALLE
    url(r'^xls_stock$', views.export_xls_stock, name='productos'),
    #1.4 Kardex RESUMEN
    url(r'^xls_proddetalle$', views.export_xls_proddetalle, name='productos'),
    
    #1.5 Proveedores
    
    url(r'^xls_control_pagos$', views.export_xls_control_pagos, name='proveedores'),

    #2. Lista Materiales 
    url(r'^export_xls$', views.export_users_xls, name='materiales'),
    #2.3 Kerdex Resumen
    url(r'^xls_stock_mat$', views.export_xls_stock_mat, name='materiales'),
    #2.4 Kerdex Detalle
     url(r'^xls_matdetalle$', views.export_xls_matdetalle, name='materiales'),
   
  
    

]
