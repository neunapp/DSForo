# -*- coding: utf-8 -*-
from django import forms
#
from captcha.fields import CaptchaField

#models
from .models import Suggestion, Tiket


class SuggestionForm(forms.ModelForm):
    """
    formulario para registrar sugerencias
    """

    captcha = CaptchaField()
    class Meta:
        model = Suggestion
        fields = (
            'email',
            'fullname',
            'description',
            'suggestion',
        )
        widgets = {
            'email': forms.TextInput(
                attrs={
                    'class':'ms-in-1__txt color-ct-c1 color-bg-b7',
                    'placeholder': 'E-mail',
                }
            ),
            'fullname': forms.TextInput(
                attrs={
                    'class':'ms-in-1__txt color-ct-c1 color-bg-b7',
                    'placeholder': 'Nombres y Apelldos',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class':'ms-in-1__txt color-ct-c1 color-bg-b7',
                    'placeholder': 'Torneo / Equipo',
                }
            ),
            'suggestion': forms.Textarea(
                attrs={
                    'class':'ms-in-1__txt color-ct-c1 color-bg-b7',
                    'placeholder': 'Sugerencia',
                    'rows': '2',
                }
            ),
        }


class TiketAddForm(forms.ModelForm):
    """
    formulario para registrar tiket
    """

    captcha = CaptchaField()
    class Meta:
        model = Tiket
        fields = (
            'tipo',
            'subject',
            'message',
        )
        widgets = {
            'tipo': forms.Select(
                attrs={
                    'class':'ms-in-1__txt color-ct-c1 color-bg-b7',
                    'placeholder': 'E-mail',
                }
            ),
            'subject': forms.TextInput(
                attrs={
                    'class':'ms-in-1__txt color-ct-c1 color-bg-b7',
                    'placeholder': 'Asunto',
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class':'ms-in-1__txt color-ct-c1 color-bg-b7',
                    'placeholder': 'Escribe tu Mensaje',
                    'rows': '4',
                }
            ),
        }
