# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.core.urlresolvers import resolve
from django.utils.translation import gettext_lazy as _

class Meta(models.Model):
    path_info = models.CharField(u"URL de la page", max_length=250, unique=True, 
            help_text=_('This can be a URL or a URL name. Ex.: "/contact/" or "website-contact"'))
    title     = models.CharField(u"Titre de page", max_length=250, blank=True, null=True, 
            help_text=_('A page title. It will show up in search engine search results.'))
    keywords  = models.CharField(u"Mots clés", max_length=250, blank=True, null=True, 
            help_text=_('Keywords separated by spaces.'))
    desc      = models.TextField(u"Description", blank=True, null=True, 
            help_text=_('A short description for the page. This will show up in search engine search results and it should not be longer than 150 characters.'))
    extra_js  = models.TextField(u"JavaScript", blank=True, null=True, 
            help_text=_('Extra JavaScript to inject into page, for example campaign tracking code (script tags must be included).'))

    def __unicode__(self):
        return _("SEO meta for %(path)s") % {'path': self.path_info}
