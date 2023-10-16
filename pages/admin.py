from django.contrib import admin
from .models import Page

# Extra Configuration
class PageAdmin(admin.ModelAdmin):
    readonly_fields= ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'created_at',)
    ordering = ('created_at',)
# Register your models here.
admin.site.register(Page, PageAdmin)

# Configuracion del Panel
title = "Django Project"
subtitle = "Panel Management"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle