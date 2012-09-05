# -*- coding: utf-8 -*-

from django.contrib import admin
from seoutils.contrib.google.webmastertools.models import WebmastertoolsFile


class WebmastertoolsFileAdmin(admin.ModelAdmin):
    list_display   = ('code', 'slug', 'is_active')
    search_fields = ('code', 'slug',)
    list_filter = ('is_active',)
    exclude = ('slug',)
admin.site.register(WebmastertoolsFile, WebmastertoolsFileAdmin)
