from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^marcar/(?P<pk>\d+)/$', views.marcar_turno, name="marcar_turno"),
]

urlpatterns += [
    url(r'^turno/form/$', views.TurnoSupraForm.as_view(), name="turno"),
    url(r'^turno/list/$', views.TurnoSupraList.as_view(), name="turno_list"),
    url(r'^turno/form/(?P<pk>\d+)/$',
        views.TurnoSupraForm.as_view(), name="turno_edit"),
]

urlpatterns += [
    url(r'^produccion/form/$', views.ProduccionSupraForm.as_view(), name="produccion"),
    url(r'^produccion/list/$', views.ProduccionSupraList.as_view(), name="produccion_list"),
    url(r'^produccion/form/(?P<pk>\d+)/$', views.ProduccionSupraForm.as_view(), name="produccion_edit"),
]

# pruebas
urlpatterns += [
    url(r'^probar/turnos/$', views.probar_turnos, name="produccion"),
]
