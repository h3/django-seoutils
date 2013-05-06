# -*- coding: utf-8 -*-

from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from seoutils.models import VirtualFile


class VirtualFileView(View):
    def get(self, request, path):
        vf = get_object_or_404(VirtualFile, url=path)
        return HttpResponse(vf.content, content_type=vf.content_type)
