from seoutils.utils import get_meta_for_url

def meta(request):
    meta = get_meta_for_url(request.META['PATH_INFO'])
    if meta:
        return { 'meta': meta }
    else:
        return {}
