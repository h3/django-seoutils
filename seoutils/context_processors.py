from seoutils.utils import get_meta_for_request

def meta(request):
    meta = get_meta_for_request(request)
    if meta:
        return { 'meta': meta }
    else:
        return {}
