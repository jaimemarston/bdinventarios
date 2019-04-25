from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'mcotizacion', views.CotizacionViewSet)
router.register(r'cotizacion_estado', views.CotizacionEstadoViewSet)

urlpatterns = [
    url(r'^deposito$', views.DepositoList.as_view()),
    url(r'^deposito/(?P<pk>[0-9]+)$', views.DepositoDetail.as_view()),
    url(r'^articulo$', views.ArticuloList.as_view()),
    url(r'^articulo/(?P<pk>[0-9]+)$', views.ArticuloDetail.as_view()),

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

    url(r'^clientesdireccion$', views.ClientesDireccionlist.as_view()),
    url(r'^clientesdirecciondetail$', views.ClientesDireccionlistdetail.as_view()),
    url(r'^', include(router.urls)),

    url(r'^banco$', views.BancoList.as_view()),
    url(r'^generate_pdf$', views.GeneratePDFCotizacionesDetail.as_view()),
    url(r'^generate_pdf/(?P<pk>\d+)/$', views.GeneratePDFCotizacionesDetail.as_view()),
    url(r'^generate_html$', TemplateView.as_view(template_name="gestionapp/invoice.html"))
]
