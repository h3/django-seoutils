from django.core.urlresolvers import resolve
from seoutils.models import Meta


def get_meta(**kwargs):
    args = ['path_info', 'url_name', 'view_name', 'app_name']
    for arg in args:
        if kwargs.get(arg, False):
            try:
                return Meta.objects.get(path_info=kwargs.get(arg))
            except Meta.DoesNotExist:
                pass
    return None



def get_default_meta():
    un = resolve('/').url_name
    return get_meta(url_name=un)


def get_meta_for_request(request, default=False):
    url = resolve('/')
    meta = get_meta(
            path_info=request.META['PATH_INFO'],
            url_name=url.url_name,
            view_name=url.view_name,
            app_name=url.app_name)
    if meta is None:
        if default:
            return get_default_meta()
        else:
            return None
    else:
        return meta
