from django.contrib import admin
from .models import Menu, TipoMenu

# Register your models here.

class TipoMenuAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class MenuAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'price', 'pointReviews')
    ordering = ('created', 'updated')
    search_fields = ('title', 'price')

admin.site.register(Menu, MenuAdmin)
admin.site.register(TipoMenu, TipoMenuAdmin)
