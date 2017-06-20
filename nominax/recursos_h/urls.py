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
    CajaCompensacion
"""
urlpatterns += [
    url(r'^caja/form/$', views.CajaSupraForm.as_view(), name="caja"),
    url(r'^caja/list/$', views.CargoSupraList.as_view(), name="caja_list"),
    url(r'^caja/form/(?P<pk>\d+)/$',
        views.CajaSupraForm.as_view(), name="caja_edit"),
    url(r'^caja/delete/(?P<pk>\d+)/$',
        views.CajaSupraFormDelete.as_view(), name="caja_delete"),
]
