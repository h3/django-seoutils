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
