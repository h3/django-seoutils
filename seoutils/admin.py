# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf import settings

from seoutils.models import Meta, Analytic, VirtualFile

if 'modeltranslation' in settings.INSTALLED_APPS:
    try:
        from grappellifit.admin import TranslationAdmin
        BaseAdmin = TranslationAdmin
    except:
        try:
            from modeltranslation.admin import TranslationAdmin
            BaseAdmin = TranslationAdmin
        except:
            BaseAdmin = admin.ModelAdmin
else:
    BaseAdmin = admin.ModelAdmin


class MetaAdmin(BaseAdmin):
    list_display = ('path_info', 'title', 'keywords', 'desc',)
    search_fields = ('path_info', 'title', 'keywords', 'desc')
admin.site.register(Meta, MetaAdmin)


class AnalyticAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'description', 'is_active',)
    search_fields = ('code', 'description',)
    list_filters = ('is_active',)
admin.site.register(Analytic, AnalyticAdmin)

class VirtualFileAdmin(admin.ModelAdmin):
    list_display = ('url', 'is_active')
    search_fields = ('url', 'content')
admin.site.register(VirtualFile, VirtualFileAdmin)
