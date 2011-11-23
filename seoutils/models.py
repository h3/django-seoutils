# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Meta(models.Model):
    path_info = models.CharField(u"URL de la page", max_length=250, unique=True)
    title     = models.CharField(u"Titre de page", max_length=250, blank=True, null=True)
    keywords  = models.CharField(u"Mots clés", max_length=250, blank=True, null=True)
    desc      = models.TextField(u"Description", blank=True, null=True)
    extra_js  = models.TextField(u"JavaScript", blank=True, null=True)

#class PageMeta(models.Model):
#    site_url        = models.CharField(u"URL de la page", max_length=250, help_text=u"Utilisé seulement à titre indicatif")
#    title           = models.CharField(u"Titre de page", max_length=250, blank=True, null=True, help_text=u"Le titre qui apparaîtera dans le \"titlebar\" du navigateur")
#    keywords        = models.CharField(u"Mots clés", max_length=250, blank=True, null=True, help_text=u"Séparés par des virgules, ex: gazon, tourbe, béton")
#    desc            = models.TextField(u"Description", blank=True, null=True)
##   extra_js        = models.TextField(u"JavaScript", blank=True, null=True)
#    content_type    = models.ForeignKey(ContentType, verbose_name=u"Type de contenu")
#    object_id       = models.PositiveIntegerField(u"ID de l'objet")
#    content_object  = generic.GenericForeignKey('content_type', 'object_id')
#
#    class Meta:
#        unique_together = ("object_id", "content_type")
#
