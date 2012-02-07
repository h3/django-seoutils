from django.core.urlresolvers import resolve
from seoutils.models import Meta

def get_meta_for_request(request):
    try:
        return Meta.objects.get(path_info=request.META['PATH_INFO'])
    except Meta.DoesNotExist:
        try:
            url_name = resolve(request.get_full_path()).url_name
            return Meta.objects.get(path_info=url_name)
        except Meta.DoesNotExist:
            try:
                return Meta.objects.get(path_info='/')
            except Meta.DoesNotExist:
                return None
            return None
    return None


