# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
#django library
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    ListView,
    TemplateView,
    View,
)

# import app canchas
from applications.miscelanea.models import Theme, Category

# import local app
from .models import Home
#

class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        #contexto principal
        #recuperamos pagina principal de la bd
        context['home'] = Home.objects.all()[0]
        context['categorias'] = Category.objects.prefetch_related('themes')
        return context
