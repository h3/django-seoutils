# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from seoutils.contrib.google.webmastertools.views import WebmastertoolsFileView

urlpatterns=patterns('',
    url(r'^google(?P<slug>[\d\w]+).html$',
        WebmastertoolsFileView.as_view(),
        name="seoutils-google-webmastertools-file"),
)
