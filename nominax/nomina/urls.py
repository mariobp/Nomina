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
    url(r'^descuento/list/$', views.DescuentoSupraList.as_view(), name="descuento_list"),
    url(r'^descuento/form/(?P<pk>\d+)/$',
        views.DescuentoSupraForm.as_view(), name="descuento_edit"),
    url(r'^descuento/delete/(?P<pk>\d+)/$',
        views.DescuentoSupraFormDelete.as_view(), name="descuento_delete"),
]