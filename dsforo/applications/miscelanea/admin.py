from django.contrib import admin
#
from .models import Category, Tag, Theme

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Theme)
