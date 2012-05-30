from django.conf.urls.defaults import *

def dummy_view(request):
    return ''

urlpatterns=patterns('',
    url(r'^$', dummy_view, name='test-home'),
    url(r'^contact/$', dummy_view, name='test-contact'),
)

