from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^historial/$', views.NominaSupraList.as_view(), name="nomina_list"),
    url(r'^corte/list/$', views.CorteSupraList.as_view(), name="corte_list"),
]
