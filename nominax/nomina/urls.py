from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^historial/$', views.NominaSupraList.as_view(), name="nomina_list"),
    url(r'^corte/list/$', views.CorteSupraList.as_view(), name="corte_list"),
    url(r'^send/mail/$', views.SendMailSupraList.as_view(), name="corte_list"),
]

"""
    Descuento urls
"""
urlpatterns = urlpatterns + [
    url(r'^descuento/form/$', views.DescuentoSupraForm.as_view(), name="descuento"),
    url(r'^finalizar/descuento/form/(?P<pk>\d+)/$', views.FinalizarDescuentoSupraForm.as_view(), name="finalizar_descuento"),
    url(r'^descuento/list/$', views.DescuentoSupraList.as_view(), name="descuento_list"),
    url(r'^descuento/form/(?P<pk>\d+)/$', views.DescuentoSupraForm.as_view(), name="descuento_edit"),
    url(r'^descuento/delete/(?P<pk>\d+)/$', views.DescuentoSupraFormDelete.as_view(), name="descuento_delete"),
]
"""
    DescuentoProduccion urls
"""
urlpatterns = urlpatterns + [
    url(r'^descuento/produccion/form/$', views.DescuentoProduccionSupraForm.as_view(), name="descuento_produccion"),
    url(r'^descuento/produccion/list/$', views.DescuentoProduccionSupraList.as_view(), name="descuento_produccion_list"),
    url(r'^descuento/produccion/form/(?P<pk>\d+)/$', views.DescuentoProduccionSupraForm.as_view(), name="descuento_produccion_edit"),
    url(r'^descuento/produccion/delete/(?P<pk>\d+)/$', views.DescuentoProduccionSupraFormDelete.as_view(), name="descuento_produccion_delete"),
]
"""
    TipoIncapacidad urls
"""
urlpatterns = urlpatterns + [
    url(r'^tipo/incapacidad/form/$', views.TipoIncapacidadSupraForm.as_view(), name="tipo_incapacidad"),
    url(r'^tipo/incapacidad/list/$', views.TipoIncapacidadSupraList.as_view(), name="tipo_incapacidad_list"),
    url(r'^tipo/incapacidad/form/(?P<pk>\d+)/$', views.TipoIncapacidadSupraForm.as_view(), name="tipo_incapacidad_edit"),
]
"""
    PagoIncapacidad urls
"""
urlpatterns = urlpatterns + [
    url(r'^pago/incapacidad/form/$', views.PagoIncapacidadSupraForm.as_view(), name="pago_incapacidad"),
    url(r'^pago/incapacidad/list/$', views.PagoIncapacidadSupraList.as_view(), name="pago_incapacidad_list"),
    url(r'^pago/incapacidad/form/(?P<pk>\d+)/$', views.PagoIncapacidadSupraForm.as_view(), name="pago_incapacidad_edit"),
]
"""
    DiaIncapacidad urls
"""
urlpatterns = urlpatterns + [
    url(r'^dia/incapacidad/form/$', views.DiaIncapacidadSupraForm.as_view(), name="dia_incapacidad"),
    url(r'^dia/incapacidad/list/$', views.DiaIncapacidadSupraList.as_view(), name="dia_incapacidad_list"),
    url(r'^dia/incapacidad/form/(?P<pk>\d+)/$', views.DiaIncapacidadSupraForm.as_view(), name="dia_incapacidad_edit"),
]