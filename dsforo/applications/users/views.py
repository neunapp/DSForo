# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from applications.variables import FULL_DOMAIN
# django
from datetime import datetime
from django.core.mail import send_mail
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
# applications
from applications.entradas.models import Entry
from applications.tiket.models import Tiket
#
from .models import User
#
from .forms import UserAddForm, LoginForm, UserUpdateForm, ResetForm

# fuciones para aplicacion usuario
import string
import random

#
def code_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class UserCreateView(CreateView):
    """ vista para registrar usuarios """

    template_name = 'users/register.html'
    success_url = reverse_lazy('users_app:panel')
    form_class = UserAddForm

    def form_valid(self, form):
        #recuperamos el usuario y guardamos
        usuario = form.save(commit=False)
        #
        codigo = code_generator()
        #
        password = form.cleaned_data['password1']
        usuario.codregistro = codigo
        usuario.set_password(password)
        usuario.save()
        user = authenticate(
            username = form.cleaned_data['email'],
            password = form.cleaned_data['password1'],
        )
        #hacemos login de usuario
        login(self.request, user)
        # enviamos mensje de correo email
        url_verificacion = FULL_DOMAIN + '/verificar-user/' + str(user.id) + '/usuario-dsforo/' + codigo + '/ds-verificacion-codigo/email-verification/'
        send_mail('DeporStart Foro - Registro', 'Confirme su Email aqui: ' + url_verificacion, 'deporstart.servicios@gmail.com', [user.email,])
        return super(UserCreateView, self).form_valid(form)



class VerificarUserView(TemplateView):
    template_name = 'users/verificar.html'

    def get_context_data(self, **kwargs):
        context = super(VerificarUserView, self).get_context_data(**kwargs)
        #contexto principal
        user = User.objects.get(id=self.kwargs['pk'])
        if user.codregistro == self.kwargs['codigo']:
            user.verificado = True
            user.save()
        return context



class UserUpdateView(LoginRequiredMixin, FormView):
    model = User
    form_class = UserUpdateForm
    login_url = reverse_lazy('users_app:login')
    success_url = reverse_lazy('users_app:panel')
    template_name = 'users/datos.html'

    def get_initial(self, **kwargs):
        # recuperamos el objeto equipo
        initial = super(UserUpdateView, self).get_initial()
        usuario = self.request.user
        #
        initial['full_name'] = usuario.full_name
        initial['image'] = usuario.image
        return initial

    def form_valid(self, form):
        #recuperamos el usuario y guardamos
        usuario = self.request.user
        # verificamos si la nueva contraseña es correcta
        user = authenticate(
            username = usuario.email,
            password = form.cleaned_data['password1'],
        )
        if user:
            passw2 = str(form.cleaned_data['password2'])
            usuario.set_password(passw2)
            usuario.save()
        #antes de actualizar imagen borramos imagen
        if (usuario.image != form.cleaned_data['image']):
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


class ResetPassword(FormView):
    """ Cambiar password de usuario """

    template_name = 'users/reset-password.html'
    success_url = reverse_lazy('users_app:login')
    form_class = ResetForm

    def form_valid(self, form):
        # Verfiamos si el usuario y contrasenha son correctos.
        codigo = code_generator()
        try:
            usuario = User.objects.get(email=form.cleaned_data['email'])
            if usuario:
                send_mail('DeporStart Foro - Reset Contraseña', 'Esta es tu nueva contraseña: ' + codigo, 'deporstart.servicios@gmail.com', [usuario.email,])
                usuario.set_password(codigo)
                usuario.save()
        except:
            print('email no valido')

        return super(ResetPassword, self).form_valid(form)


class LogoutView(View):
    """
    cerrar sesion
    """
    url = '/auth/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:login'
            )
        )


class PanelView(LoginRequiredMixin, ListView):
    """ vista para panel principal de usuarios"""

    login_url = reverse_lazy('users_app:login')
    context_object_name = 'entradas'
    template_name = 'users/panel.html'

    def get_queryset(self):
        usuario = self.request.user
        query_set = Entry.objects.filter(
            user=usuario,
            anulate=False
        ).order_by('-created')
        return query_set


class PanelTiketView(LoginRequiredMixin, ListView):
    """ vista para ver los tikets enviados por un usuario"""

    login_url = reverse_lazy('users_app:login')
    context_object_name = 'tikets'
    template_name = 'users/mis-tikets.html'

    def get_queryset(self):
        usuario = self.request.user
        query_set = Tiket.objects.filter(
            user=usuario,
            anulate=False
        ).order_by('-created')
        return query_set
