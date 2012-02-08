# -*- coding: utf-8 -*-

from django.conf import settings
from django import template
from django.contrib.contenttypes.models import ContentType
from django.template import Library, Node, TemplateSyntaxError
from django.template import Variable, resolve_variable
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from seoutils.models import Meta
from seoutils.utils import get_meta_for_request

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


class OldMetaForUrlNode(Node):
    def __init__(self, obj, context_var=False, prop=False):
        print "wARNING: The template tag \"seometa_for_url\" is deprecated and will be eventually removed. Please use the \"seometa\" tag instead."
        self.prop = prop
        self.obj = Variable(obj)
        self.context_var = context_var
 
    def render(self, context):
        rs  = False
        url = self.obj.resolve(context)
        try:
            rs = Meta.objects.get(path_info=url)
        except Meta.DoesNotExist:
            try:
                rs = Meta.objects.get(path_info='/')
            except Meta.DoesNotExist:
                if self.context_var:
                    context[self.context_var] = ''
                return ''
        finally:
            if rs:
                if self.prop:
                    rs = getattr(rs, self.prop, '')
                    if not rs:
                        try:
                            rs = Meta.objects.get(path_info='/')
                            rs = getattr(rs, self.prop, '')
                        except Meta.DoesNotExist:
                            if self.context_var:
                                context[self.context_var] = ''
                            return ''
                if self.context_var:
                    context[self.context_var] = rs
                    return ''
                else:
                    return rs
        return ''

def seometa_for_url(parser, token):
    """
    {% seometa_for_url 'http://www.google.ca/' as seometa %}
    {{ seometa.title }}
    {{ seometa.description }}
    """
    try:
        bits = token.split_contents()
    except ValueError:
        raise TemplateSyntaxError('tag requires exactly two arguments')
 
    if len(bits) == 5:
        # seometa_for_url <url> <property> as <variable>
        return OldMetaForUrlNode(bits[1], bits[4], bits[2])
    elif len(bits) == 4:
        # seometa_for_url <url> as <variable>
        return OldMetaForUrlNode(bits[1], bits[3])
    elif len(bits) == 3:
        # seometa_for_url <url> <property>
        return OldMetaForUrlNode(bits[1], False, bits[2])
 
register.tag('seometa_for_url', seometa_for_url)


