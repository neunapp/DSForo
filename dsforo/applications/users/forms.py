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
                'class': 'form-item__input',
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
                'class': 'form-item__input',
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
                'class': 'form-item__input',
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            'email',
        )
        #
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'E-mail',
                    'class': 'form-item__input',
                }
            ),
        }



class UserForm(forms.ModelForm):
    """ formulario para usuarios """

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'image',
            'gender',
            'phone',
            'date_birth',
        )
        #
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombres',
                    'class': 'form-item__input',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Apellidos',
                    'class': 'form-item__input',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Numero de telefono celular',
                    'class': 'form-item__input',
                }
            ),
            'date_birth': forms.DateInput(
                attrs={
                    'class': 'form-item__input',
                    'type': 'date',
                }
            ),
        }
    #
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) < 2:
            msj = 'Ingrese un nombre correcto'
            self.add_error('first_name', msj)
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if len(last_name) < 2:
            msj = 'Ingrese un apellido correcto'
            self.add_error('last_name', msj)
        return last_name

    def clean_gender(self):
        gender = self.cleaned_data['gender']
        if gender == '':
            msj = 'Seleccione esta opcion'
            self.add_error('gender', msj)
        return gender


    def clean_image(self):
        image = self.cleaned_data['image']
        if type(image) == TemporaryUploadedFile:
            if image:
                if image._size > 4*1024*1024:
                    self.add_error('image', 'La imagen es muy grande')
        #
        return image


    def clean_date_birth(self):
        date_birth = self.cleaned_data['date_birth']
        if date_birth != None:
            end_date = timezone.now().date()
            start_date = end_date - timedelta(days=30)
            if date_birth > start_date:
                msj = 'La fecha no es posible'
                self.add_error('date_birth', msj)
            else:
                print('fecha correcta')
        else :
            msj = 'Ingrese una fecha valida'
            self.add_error('date_birth', msj)
        return date_birth
