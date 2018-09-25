# -*- coding: utf-8 -*-
from django.urls import reverse_lazy, reverse
from django.contrib.sitemaps import Sitemap
import datetime
#import models
from applications.entradas.models import Entry
from applications.miscelanea.models import Category, Theme

class EntrySitemap(Sitemap):
    """ sitemap para Entry """
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
       return Entry.objects.filter(anulate=False)

    def lastmod(self, obj):
        return obj.created


class Sitemap(Sitemap):
    """ sitemap para url staticas """
    protocol = 'https'

    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names

    def changefreq(self, obj):
        return 'weekly'

    def lastmod(self, obj):
        return datetime.datetime.now()

    def location(self, obj):
        return reverse_lazy(obj)
