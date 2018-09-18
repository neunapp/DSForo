# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#
from .models import Tiket, Suggestion

#


class TiketAdmin(admin.ModelAdmin):

    """admin model Tiket"""
    list_display = (
        'subject',
        'tipo',
        'message',
        'id',
    )
    #
    search_fields = ('subject',)
    list_filter = ('tipo',)


class SuggestionAdmin(admin.ModelAdmin):

    """admin model Suggestion"""
    list_display = (
        'email',
        'fullname',
        'description',
        'id',
    )
    #
    search_fields = ('email',)

admin.site.register(Tiket, TiketAdmin)
admin.site.register(Suggestion, SuggestionAdmin)
