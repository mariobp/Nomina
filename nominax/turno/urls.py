from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^marcar/$', views.marcar_turno, name="marcar_turno"),
]