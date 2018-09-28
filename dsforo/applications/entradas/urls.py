# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

app_name="entradas_app"

urlpatterns = [
    #
    #url para pantalla de inicio
    url(r'^como-organizar-un-campeonato-de-futbol/$',
        views.SearchEntryView.as_view(),
        name='entry_search'
    ),
    #url para lista de entradas por categoria
    url(r'^nuevo-tema-de-foro/(?P<pk>\d+)/$',
        views.EntryCreateView.as_view(),
        name='entrada_add'
    ),
	#url para lista de entradas por categoria
    url(r'^ds/(?P<slug>[-\w]+)/$',
        views.ListaEntradasView.as_view(),
        name='entradas_por_tema'
    ),
    # url para el detalle de una entrada
    url(r'^ds/entrada/(?P<slug>[-\w]+)/$',
        views.EntryDetailView.as_view(),
        name='entrada_detalle'
    ),
    # url para eliminar una entrada
    url(
        r'^mis-entradas/delete/(?P<pk>\d+)/eliminar-entrada-seleccionado/$',
        views.EntryDeleteView.as_view(),
        name='entrada_delete'
    ),
    #url para pantalla de inicio
    url(r'^dsnoticias/noticias-deportivas-de-futbol-peruano/$',
        views.ListaNewsView.as_view(),
        name='news_list'
    ),
    #
    url(
        r'^dsnoticias/detalle/(?P<slug>[-\w]+)$',
        views.NewsDetailView.as_view(),
        name='noticias_detalle'
    ),
]
