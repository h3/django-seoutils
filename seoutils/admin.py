# -*- coding: utf-8 -*-

from django.contrib import admin
from seoutils.models import Meta

#class PageMetaAdmin(admin.ModelAdmin):
#    list_display   = ('site_url', 'title', 'keywords', 'desc',)
#admin.site.register(PageMeta, PageMetaAdmin)



try:
    from grappellifit.admin import TranslationAdmin
    BaseAdmin = TranslationAdmin
except:
    try:
        from modeltranslation.admin import TranslationAdmin
        BaseAdmin = TranslationAdmin
    except:
        BaseAdmin = admin.ModelAdmin


class MetaAdmin(BaseAdmin):
    list_display   = ('path_info', 'title', 'keywords', 'desc',)
    search_fields = ('path_info', 'title', 'keywords', 'desc')

admin.site.register(Meta, MetaAdmin)
