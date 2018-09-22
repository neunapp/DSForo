from django.contrib import admin

from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):

    """admin model Entry"""
    list_display = (
        'email',
        'full_name',
        'id',
        'verificado',
    )
    #
    search_fields = ('email', 'full_name')
    list_filter = ('verificado',)


admin.site.register(User, UserAdmin)
