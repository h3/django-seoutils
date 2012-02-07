from django.core.urlresolvers import reverse, resolve
from django.template import RequestContext
from webcore.contrib.frontadmin.plugins import PluginBase

class Plugin(PluginBase):

    def get_context(self):
        context = RequestContext(self.request)
        url_name = resolve(self.request.get_full_path()).url_name
        if 'meta' in context:
            meta = context['meta']

            if not meta.exists(self.request):
                url = reverse('admin:seoutils_meta_add') + '?inject=id_path_info&value='+ url_name
            else:
                url = reverse('admin:seoutils_meta_change', args=[meta.pk])
        else:
            url = reverse('admin:seoutils_meta_add') + '?inject=id_path_info&value='+ url_name

        return self.button(
                id="frontadmin-meta", 
                url=url, 
                classname="frontadmin-change-object",
                label="Meta", 
                title="Edit Metas for this page")
