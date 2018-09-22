# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

app_name="tiket_app"

urlpatterns = [
	# url para lregistrar una sugerencia de tema
    url(r'^enviar-sugerencia/$',
        views.SuggestionCreateView.as_view(),
        name='add_sugerencia'
    ),
    # url para registrar un tiket
    url(r'^enviar-nuevo-tiket/$',
        views.TiketCreateView.as_view(),
        name='add_tiket'
    ),
    # url para eliminar un tiket
    url(
        r'^mis-tiket/delete/(?P<pk>\d+)/eliminar-tiket-seleccionado/$',
        views.TiketDeleteView.as_view(),
        name='tiket_delete'
    ),
]
