# -*- encoding: utf-8 -*-
from PIL import Image
from django import forms

from datetime import datetime, timedelta
from django.utils import timezone

from django.contrib.auth import authenticate
from django.core.files.uploadedfile import TemporaryUploadedFile

#app user
from .models import User


class LoginForm(forms.Form):

    email = forms.CharField(
        label='Email',
        max_length='100',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'E-mail',
                'name':'email',
                'class': 'ms-in-1__txt color-ct-c1 color-bg-b7',
                'autofocus': 'autofocus',
            }
        ),
    )
    password = forms.CharField(
        label='contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password',
                'class': 'ms-in-1__txt color-ct-c1 color-bg-b7',
            }
        ),
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('email o password incorrectos.')
        return self.cleaned_data


class UserAddForm(forms.ModelForm):
    """ formulario para registrar usuarios """

    password1 = forms.CharField(
        label='contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'contraseña nueva',
                'class': 'ms-in-1__txt color-ct-c1 color-bg-b7',
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            'email',
            'full_name',
        )
        #
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'E-mail',
                    'class': 'ms-in-1__txt color-ct-c1 color-bg-b7',
                }
            ),
            'full_name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombres',
                    'class': 'ms-in-1__txt color-ct-c1 color-bg-b7',
                }
            ),
        }



class UserUpdateForm(forms.ModelForm):
    """ formulario para modificar usuarios """

    password1 = forms.CharField(
        label='contraseña',
        required=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'contraseña actual',
                'class': 'ms-in-1__txt color-ct-c1 color-bg-b7',
            }
        ),
    )
    password2 = forms.CharField(
        label='contraseña nueva',
        required=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'contraseña nueva',
                'class': 'ms-in-1__txt color-ct-c1 color-bg-b7',
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            'full_name',
            'image',
        )
        #
        widgets = {
            'full_name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombres',
                    'class': 'ms-in-1__txt color-ct-c1 color-bg-b7',
                }
            ),
        }
    #
    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        if len(full_name) < 2:
            msj = 'Ingrese un nombre correcto'
            self.add_error('full_name', msj)
        return full_name


    def clean_image(self):
        image = self.cleaned_data['image']
        if type(image) == TemporaryUploadedFile:
            if image:
                if image._size > 4*1024*1024:
                    self.add_error('image', 'La imagen es muy grande')
        #
        return image


class ResetForm(forms.Form):

    email = forms.CharField(
        label='Email',
        max_length='100',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'E-mail',
                'name':'email',
                'class': 'ms-in-1__txt color-ct-c1 color-bg-b7',
                'autofocus': 'autofocus',
            }
        ),
    )
