# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

from seoutils.views import VirtualFileView

urlpatterns=patterns('',
    url(r'^(?P<path>.*)$', VirtualFileView.as_view(), name='seoutils-virtualfile'),
)
