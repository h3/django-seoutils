# -*- coding: utf-8 -*-

from django.conf import settings
from django import template
from django.contrib.contenttypes.models import ContentType
from django.template import Library, Node, TemplateSyntaxError
from django.template import Variable, resolve_variable
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from seoutils.models import Meta, Analytic
from seoutils.utils import get_meta_for_request
from django.utils.safestring import mark_safe
register = template.Library()


class MetaForUrlNode(Node):
    def __init__(self, request, context_var=False):
        self.request = Variable(request)
        self.context_var = context_var
 
    def render(self, context):
        rs  = False
        request = self.request.resolve(context)
        context[self.context_var] = get_meta_for_request(request)
        return ''


def seometa(parser, token):
    """
    Example usage:
    {% seometa request as seometa %}
    {{ seometa.title }}
    {{ seometa.description }}
    {{ seometa.extra_js|safe }}
    """
    try:
        bits = token.split_contents()
    except ValueError:
        raise TemplateSyntaxError('seometa tag requires exactly three arguments')
    if len(bits) != 4:
        raise TemplateSyntaxError('seometa tag requires exactly three arguments')
    return MetaForUrlNode(bits[1], bits[3])
register.tag('seometa', seometa)


@register.assignment_tag()
def get_analytics():
    out = []
    for a in Analytic.objects.filter(is_active=True):
        out.append(a.code)
    return mark_safe(''.join(out))
