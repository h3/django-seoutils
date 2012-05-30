from django.core.urlresolvers import resolve, reverse, NoReverseMatch
from seoutils.models import Meta


def get_default_meta():
    try:
        un = resolve('/').url_name
        return get_meta(url_name=un, path_info='/', fallback=False)
    except:
        return None


def get_meta(**kwargs):
    meta = None
    args = ['path_info', 'url_name', 'view_name', 'app_name']
    for arg in args:
        if kwargs.get(arg, False):
            try:
                meta = Meta.objects.get(path_info=kwargs.get(arg))
            except Meta.DoesNotExist:
                pass

    # Here we use the root url title/keywords/description
    # if they are blank in this meta, not that the meta is
    # not saved intentionnaly. Yes, it's ugly as fuck.
    if meta and not kwargs.get('fallback', True) is False:
        if meta.keywords is None or meta.keywords == '' \
            or meta.title is None or meta.title == '' \
            or meta.desc is None or meta.desc == '':
            default_meta = get_default_meta()
            if default_meta:
                if meta.title is None or meta.title == '': 
                    meta.title = default_meta.title
                if meta.keywords is None or meta.keywords == '': 
                    meta.keywords = default_meta.keywords
                if meta.desc is None or meta.desc == '': 
                    meta.desc = default_meta.desc
    return meta


def get_meta_for_request(request, default=False):
    try:
        url = resolve(request.META['PATH_INFO'])
    except:
        return None
    meta = get_meta(
            path_info=request.META['PATH_INFO'],
            url_name=url.url_name,
            view_name=url.view_name)

    if meta is None:
        try:
            if reverse(url.url_name) != '/':
                return get_default_meta()
            else:
                return None
        except NoReverseMatch:
            return None

    return meta
