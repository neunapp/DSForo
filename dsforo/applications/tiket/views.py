# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
#django library
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    ListView,
    TemplateView,
    View,
)
from django.core.mail import send_mail

#
from applications.entradas.models import Entry
#
from .forms import SuggestionForm, TiketAddForm
# import local app
from .models import Tiket, Suggestion
#

class SuggestionCreateView(CreateView):
    model = Suggestion
    form_class = SuggestionForm
    success_url = reverse_lazy('home_app:index')
    template_name = 'tiket/sugerencia_add.html'

    def get_context_data(self, **kwargs):
        context = super(SuggestionCreateView, self).get_context_data(**kwargs)
        #contexto principal
        #recuperamos pagina principal de la bd
        context['populares'] = Entry.objects.filter(
            theme__tipo='2',
            anulate=False
        ).order_by('-vists')[:15]
        return context


class TiketCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users_app:login')
    model = Tiket
    form_class = TiketAddForm
    success_url = reverse_lazy('users_app:panel-tikets')
    template_name = 'tiket/tiket_add.html'

    def get_context_data(self, **kwargs):
        context = super(TiketCreateView, self).get_context_data(**kwargs)
        #contexto principal
        #recuperamos pagina principal de la bd
        context['populares'] = Entry.objects.filter(
            theme__tipo='2',
            anulate=False
        ).order_by('-vists')[:15]
        return context

    def form_valid(self, form):
        tiket = form.save(commit=False)
        tiket.user = self.request.user
        #
        tiket.save()
        #
        send_mail('DS Foro - Tiket', 'Email: ' + tiket.user.email + 'Mensaje: ' + tiket.message, 'deporstart.servicios@gmail.com', ['deporstart.servicios@gmail.com',])
        return super(TiketCreateView, self).form_valid(form)


class TiketDeleteView(LoginRequiredMixin, DeleteView):
    '''
    Eliminar Tiket.
    '''
    login_url = reverse_lazy('users_app:login')
    model = Tiket
    success_url = reverse_lazy('users_app:panel-tikets')
    template_name = 'tiket/delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        #desabilitamos Conductor
        self.object.anulate = True
        self.object.save()
        success_url = self.get_success_url()

        return HttpResponseRedirect(success_url)
