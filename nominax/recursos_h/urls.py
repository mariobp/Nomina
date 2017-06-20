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
