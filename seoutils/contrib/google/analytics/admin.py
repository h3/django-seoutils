# -*- coding: utf-8 -*-

from django.contrib import admin
from seoutils.contrib.google.analytics.models import AnalyticCode


class AnalyticCodeAdmin(admin.ModelAdmin):
    list_display   = ('code', 'note', 'is_active')
    search_fields = ('code', 'note',)
    list_filter = ('is_active',)
admin.site.register(AnalyticCode, AnalyticCodeAdmin)
