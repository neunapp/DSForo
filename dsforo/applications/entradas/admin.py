# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#
from .models import Entry, Comentary

#


class EntryAdmin(admin.ModelAdmin):

    """admin model Entry"""
    list_display = (
        'title',
        'user',
        'id',
    )
    #
    filter_horizontal = ('tag',)
    search_fields = ('title',)
    list_filter = ('theme',)


class ComentaryAdmin(admin.ModelAdmin):

    """admin model Comentary"""
    list_display = (
        'entry',
        'user',
        'id',
    )
    #

admin.site.register(Entry, EntryAdmin)
admin.site.register(Comentary, ComentaryAdmin)
