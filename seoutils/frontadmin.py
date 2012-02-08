from django.core.urlresolvers import reverse, resolve
from django.template import RequestContext

from webcore.contrib.frontadmin.plugins import PluginBase
from seoutils.utils import get_meta_for_request

class Plugin(PluginBase):

    def get_context(self):
        # TODO: here we should use the context to resolve the meta object
        # instead of hitting the database again
        # print RequestContext(self.request)
        meta = get_meta_for_request(self.request)
        url_name = resolve(self.request.get_full_path()).url_name
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
