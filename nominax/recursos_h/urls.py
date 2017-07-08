from django.conf.urls import include, url
import views

"""
    Cargo urls
"""
urlpatterns = [
    url(r'^cargo/form/$', views.CargoSupraForm.as_view(), name="cargo"),
    url(r'^cargo/list/$', views.CargoSupraList.as_view(), name="cargo_list"),
    url(r'^cargo/form/(?P<pk>\d+)/$',
        views.CargoSupraForm.as_view(), name="cargo_edit"),
    url(r'^cargo/delete/(?P<pk>\d+)/$',
        views.CargoSupraFormDelete.as_view(), name="cargo_delete"),
]


"""
    Pension urls
"""
urlpatterns += [
    url(r'^pension/form/$', views.PensionSupraForm.as_view(), name="pension"),
    url(r'^pension/list/$', views.PensionSupraList.as_view(), name="pension_list"),
    url(r'^pension/form/(?P<pk>\d+)/$',
        views.PensionSupraForm.as_view(), name="pension_edit"),
    url(r'^pension/delete/(?P<pk>\d+)/$',
        views.PensionSupraFormDelete.as_view(), name="pension_delete"),
]

"""
    Eps urls
"""
urlpatterns += [
    url(r'^eps/form/$', views.EpsSupraForm.as_view(), name="eps"),
    url(r'^eps/list/$', views.EpsSupraList.as_view(), name="eps_list"),
    url(r'^eps/form/(?P<pk>\d+)/$',
        views.EpsSupraForm.as_view(), name="eps_edit"),
    url(r'^eps/delete/(?P<pk>\d+)/$',
        views.EpsSupraFormDelete.as_view(), name="eps_delete"),
]

"""
    UnidadProduccion urls
"""
urlpatterns += [
    url(r'^unidad/produccion/form/$', views.UnidadProduccionSupraForm.as_view(), name="unidad_produccion"),
    url(r'^unidad/produccion/list/$', views.UnidadProduccionSupraList.as_view(), name="unidad_produccion_list"),
    url(r'^unidad/produccion/form/(?P<pk>\d+)/$', views.UnidadProduccionSupraForm.as_view(), name="unidad_produccion_edit"),
    url(r'^unidad/produccion/delete/(?P<pk>\d+)/$', views.UnidadProduccionSupraFormDelete.as_view(), name="unidad_produccion_delete"),
]


"""
    Tarifario
"""
urlpatterns += [
    url(r'^tarifario/form/$', views.TarifarioSupraForm.as_view(), name="tarifario"),
    url(r'^tarifario/list/$', views.TarifarioSupraList.as_view(), name="tarifario_list"),
    url(r'^tarifario/form/(?P<pk>\d+)/$', views.TarifarioSupraForm.as_view(), name="tarifario_edit"),
    url(r'^tarifario/delete/(?P<pk>\d+)/$', views.TarifarioSupraFormDelete.as_view(), name="tarifario_delete"),
]

"""
    CajaCompensacion
"""
urlpatterns += [
    url(r'^caja/form/$', views.CajaSupraForm.as_view(), name="caja"),
    url(r'^caja/list/$', views.CajaSupraList.as_view(), name="caja_list"),
    url(r'^caja/form/(?P<pk>\d+)/$', views.CajaSupraForm.as_view(), name="caja_edit"),
    url(r'^caja/delete/(?P<pk>\d+)/$', views.CajaSupraFormDelete.as_view(), name="caja_delete"),
]


"""
    Cesantia
"""

urlpatterns += [
    url(r'^cesantia/form/$', views.CesantiaSupraForm.as_view(), name="cesantia"),
    url(r'^cesantia/list/$', views.CesantiaSupraList.as_view(), name="cesantia_list"),
    url(r'^cesantia/form/(?P<pk>\d+)/$',
        views.CesantiaSupraForm.as_view(), name="cesantia_edit"),
    url(r'^cesantia/delete/(?P<pk>\d+)/$',
        views.CesantiaSupraFormDelete.as_view(), name="cesantia_delete"),
]


"""
    Tipo de contrato
"""

urlpatterns += [
    url(r'^tipo/contrato/form/$', views.TipoContratoSupraForm.as_view(), name="tipo_contrato"),
    url(r'^tipo/contrato/list/$', views.TipoContratoSupraList.as_view(), name="tipo_contrato_list"),
    url(r'^tipo/contrato/form/(?P<pk>\d+)/$',
        views.TipoContratoSupraForm.as_view(), name="tipo_contrato_edit"),
    url(r'^tipo/contrato/delete/(?P<pk>\d+)/$',
        views.TipoContratoSupraFormDelete.as_view(), name="tipo_contrato_delete"),
]

"""
    Empleado
"""

urlpatterns += [
    url(r'^empleado/form/$', views.EmpleadoSupraForm.as_view(), name="empleado"),
    url(r'^contrato/form/$', views.ContratoForm.as_view(), name="contrato"),
    url(r'^empleado/list/$', views.EmpleadoSupraList.as_view(), name="empleado_list"),
    url(r'^contrato/list/$', views.ContraoSupraList.as_view(), name="contrato_list"),
    url(r'^empleado/form/(?P<pk>\d+)/$',
        views.EmpleadoSupraForm.as_view(), name="empleado_edit"),
    url(r'^contrato/form/(?P<pk>\d+)/$',
        views.ContratoForm.as_view(), name="contrato_edit"),
]
