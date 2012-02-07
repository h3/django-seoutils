from seoutils.models import Meta

def get_meta_for_url(url):
    try:
        return Meta.objects.get(path_info=url)
    except Meta.DoesNotExist:
        return Meta.objects.get(path_info='/')
    except Meta.DoesNotExist:
        return None
