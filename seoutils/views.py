# -*- coding: utf-8 -*-

from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
#from django.views.defaults page_not_found
from django.views.decorators.csrf import requires_csrf_token

from seoutils.models import VirtualFile


# DEPRECATED!
class VirtualFileView(View):
    def get(self, request, path):
        vf = get_object_or_404(VirtualFile, url=path)
        return HttpResponse(vf.content, content_type=vf.content_type)


@requires_csrf_token
def page_not_found(request, template_name='404.html'):
    """
    SEOutils 404 handler.

    Returns a VirtualFile object from the database or fallsback
    to default behavior (404).

    Templates: :template:`404.html`
    Context:
        request_path
            The path of the requested URL (e.g., '/app/pages/bad_page/')
    """
    vf = get_object_or_404(VirtualFile, url=request.META.get('PATH_INFO')[1:])
    return HttpResponse(vf.content, content_type=vf.content_type)
