# -*- coding: utf-8 -*-

from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from seoutils.contrib.google.webmastertools.models import WebmastertoolsFile


class WebmastertoolsFileView(View, SingleObjectMixin):
    model = WebmastertoolsFile

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug=slug, is_active=True)
        return HttpResponse(u'%s' % obj.render())
