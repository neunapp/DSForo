# -*- coding: utf-8 -*-
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
#
from captcha.fields import CaptchaField

#models
from .models import Entry, Comentary


class EntryAddForm(forms.ModelForm):
    """
    formulario para registrar una nueva entrada
    """

    content = forms.CharField(widget=CKEditorUploadingWidget())
    captcha = CaptchaField()
    class Meta:
        model = Entry
        fields = (
            'title',
            'resume',
        )
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class':'ms-in-1__txt color-ct-c1 color-bg-b7',
                    'placeholder': 'Nombres y Apelldos',
                }
            ),
            'resume': forms.Textarea(
                attrs={
                    'class':'ms-in-1__txt color-ct-c1 color-bg-b7',
                    'placeholder': 'Sugerencia',
                    'rows': '2',
                }
            ),
        }
