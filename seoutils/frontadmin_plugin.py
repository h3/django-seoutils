from django.core.urlresolvers import reverse, resolve
from django.core.urlresolvers import Resolver404
from django.template import RequestContext
from django.conf import settings

from seoutils.utils import get_meta_for_request

try:
    from frontadmin.plugins import PluginBase
except:
    # DEPRECATED
    from webcore.contrib.frontadmin.plugins import PluginBase

class Plugin(PluginBase):

    def get_context(self):
        # TODO: here we should use the context to resolve the meta object
        # instead of hitting the database again
        # print RequestContext(self.request)

        if isinstance(self.request, str) or not self.request.user.has_perm("seoutils.add_meta") or \
           not self.request.user.has_perm("seoutils.change_meta") or \
           not self.request.user.has_perm("seoutils.delete_meta"):
               return ''

        meta = get_meta_for_request(self.request)

        try:
            url_name = resolve(self.request.META['PATH_INFO']).url_name
        except Resolver404:
            return ''

        if meta:
            url = reverse('admin:seoutils_meta_change', args=[meta.pk])
        else:
            url = reverse('admin:seoutils_meta_add') + '?inject=id_path_info&value='+ url_name

        return self.button(
                id="frontadmin-meta", 
                url=url, 
                classname="frontadmin-change-object",
                label="Meta", 
                title="Edit Metas for this page")
