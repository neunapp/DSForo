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
from django.views.generic.edit import FormMixin

#
from applications.miscelanea.models import Theme
# import local app
from .models import Entry, Comentary
#
from .forms import EntryAddForm, ComentaryForm
#


class SearchEntryView(ListView):
    """ vista que busca entradas"""

    context_object_name = 'entradas'
    template_name = 'entradas/search.html'

    def get_queryset(self):
        #recuperamos el valor por GET
        q = self.request.GET.get("kword", '')
        queryset = Entry.objects.search_entry(q)
        return queryset


class ListaEntradasView(ListView):
    """ listamos las entradas de un tema """

    context_object_name = 'entradas'
    template_name = 'entradas/por_tema.html'

    def get_context_data(self, **kwargs):
        context = super(ListaEntradasView, self).get_context_data(**kwargs)
        context['tema'] = Theme.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        #recuperamos el valor por GET
        slug=self.kwargs['slug']
        queryset = Entry.objects.filter(
            theme__slug=slug,
            anulate=False,
        ).order_by('-vists')
        return queryset


class EntryDetailView(FormMixin, DetailView):
    """ vista para ver una entrada """
    model = Entry
    template_name = 'entradas/ver.html'
    form_class = ComentaryForm
    success_url = '.'

    def get_queryset(self):
        qs = super(EntryDetailView, self).get_queryset().filter(anulate=False)
        return qs

    def get_context_data(self, **kwargs):
        context = super(EntryDetailView, self).get_context_data(**kwargs)
        entrada = self.get_object()
        entrada.vists = entrada.vists + 1
        entrada.save()
        comentarios = []
        if entrada.theme.tipo == '0':
            # cargamos lista de ultimos comentarios
            comentarios = Comentary.objects.filter(entry__pk=entrada.pk)[:20]
        context['comentarios'] = comentarios
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        entrada = self.get_object()
        usuario = self.request.user
        comentario = form.cleaned_data['comentario']
        Comentary(
            user=usuario,
            entry=entrada,
            content=comentario,
            calification=1,
        ).save()
        return HttpResponseRedirect(self.get_success_url())


class EntryCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users_app:login')
    model = Entry
    form_class = EntryAddForm
    success_url = reverse_lazy('users_app:panel')
    template_name = 'entradas/add_entrada.html'

    def get_context_data(self, **kwargs):
        context = super(EntryCreateView, self).get_context_data(**kwargs)
        #recuperamos pagina principal de la bd
        context['populares'] = Entry.objects.filter(
            theme__tipo='0',
            anulate=False
        ).order_by('-vists')[:15]
        return context

    def form_valid(self, form):
        entrada = form.save(commit=False)
        entrada.user = self.request.user
        thema = Theme.objects.get(
            pk=self.kwargs['pk']
        )
        entrada.theme = thema
        #
        entrada.content = form.cleaned_data['content']
        entrada.save()
        return super(EntryCreateView, self).form_valid(form)


class EntryDeleteView(LoginRequiredMixin, DeleteView):
    '''
    Eliminar Tiket.
    '''
    login_url = reverse_lazy('users_app:login')
    model = Entry
    success_url = reverse_lazy('users_app:panel')
    template_name = 'entradas/delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        #desabilitamos Conductor
        self.object.anulate = True
        self.object.save()
        success_url = self.get_success_url()

        return HttpResponseRedirect(success_url)
