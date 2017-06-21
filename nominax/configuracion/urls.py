from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^list/$', views.ConfiguracionSupraList.as_view(), name="configuracion_list"),
    url(r'^form/$', views.ConfiguracionSupraForm.as_view(), name="configuracion_form"),
    url(r'^form/(?P<pk>\d+)/$', views.ConfiguracionSupraForm.as_view(), name="configuracion_form_edit"),
]
