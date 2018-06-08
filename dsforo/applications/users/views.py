# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# django
from datetime import datetime
from django.views.generic.edit import FormView
from django.views.generic import (
    DetailView,
    TemplateView,
    DeleteView,
    UpdateView,
    ListView,
    CreateView,
    View
)
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
#app canchas
from applications.cancha.models import CanchaFrecuente

from .models import User
#
from .forms import UserAddForm, LoginForm, UserForm


class UserCreateView(CreateView):
    """ vista para registrar usuarios """

    template_name = 'users/register.html'
    success_url = reverse_lazy('users_app:panel')
    form_class = UserAddForm

    def form_valid(self, form):
        #recuperamos el usuario y guardamos
        usuario = form.save(commit=False)
        password = form.cleaned_data['password1']
        usuario.set_password(password)
        usuario.save()
        user = authenticate(
            username = form.cleaned_data['email'],
            password = form.cleaned_data['password1'],
        )
        #hacemos login de usuario
        login(self.request, user)
        return super(UserCreateView, self).form_valid(form)


class UserUpdateView(LoginRequiredMixin, FormView):
    model = User
    form_class = UserForm
    login_url = reverse_lazy('users_app:user_login')
    success_url = reverse_lazy('users_app:panel')
    template_name = 'users/update.html'

    def get_initial(self, **kwargs):
        # recuperamos el objeto equipo
        initial = super(UserUpdateView, self).get_initial()
        usuario = self.request.user
        #
        initial['first_name'] = usuario.first_name
        initial['last_name'] = usuario.last_name
        initial['date_birth'] = str(usuario.date_birth)
        initial['phone'] = usuario.phone
        initial['image'] = usuario.image
        initial['gender'] = usuario.gender
        return initial

    def form_valid(self, form):
        #recuperamos el usuario y guardamos
        usuario = self.request.user
        # actualizamos los datos de usuario
        usuario.first_name = form.cleaned_data['first_name']
        usuario.last_name = form.cleaned_data['last_name']
        usuario.phone = form.cleaned_data['phone']
        usuario.date_birth = form.cleaned_data['date_birth']
        usuario.gender = form.cleaned_data['gender']
        #antes de actualizar imagen borramos imagen
        if ((usuario.image != None) or (usuario.image == 'False')):
            usuario.image.delete()
        #
        usuario.image = form.cleaned_data['image']
        usuario.save()
        return super(UserUpdateView, self).form_valid(form)


class LogIn(FormView):
    """ vista para acceso de usuarios login """

    template_name = 'users/login.html'
    success_url = reverse_lazy('users_app:panel')
    form_class = LoginForm

    def form_valid(self, form):
        # Verfiamos si el usuario y contrasenha son correctos.
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)

        return super(LogIn, self).form_valid(form)


class LogoutView(View):
    """
    cerrar sesion
    """
    url = '/auth/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user_login'
            )
        )


class PanelView(LoginRequiredMixin, ListView):
    """ vista para panel principal de usuarios"""

    login_url = reverse_lazy('users_app:user_login')
    context_object_name = 'canchas'
    template_name = 'users/panel.html'

    def get_queryset(self):
        usuario = self.request.user
        query_set = CanchaFrecuente.objects.list_by_user(usuario)
        return query_set
