# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

app_name="home_app"

urlpatterns = [
	#url para pantalla de inicio
    url(r'^$',
        views.HomeView.as_view(),
        name='index'
    ),
]
