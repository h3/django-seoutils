# -*- coding: utf-8 -*-

import re

from django.db import models
from django.utils.translation import gettext_lazy as _

CONTENT_TYPE_CHOICES = (
    ('text/plain', _('Plain text')),
    ('text/xml', _('XML text')),
    ('text/html', _('HTML text')),
    ('application/xml', _('XML application')),
    ('application/xhtml+xml', _('XHTML application')),
)


class Meta(models.Model):
    path_info = models.CharField(_('URL of the page'), max_length=250,
            unique=True, db_index=True, help_text=_('This can be a URL or a \
URL name. Ex.: "/contact/" or "website-contact"'))

    title = models.CharField(_('Page title'), max_length=250, blank=True,
            null=True, help_text=_('A page title. It will show up in search \
engine search results.'))

    keywords = models.CharField(_('Keywords'), max_length=250, blank=True,
            null=True, help_text=_('Keywords separated by spaces.'))

    desc = models.TextField(_('Description'), blank=True, null=True,
            help_text=_('A short description for the page. This will show up \
in search engine search results and it should not be longer \
than 150 characters.'))

    extra_js = models.TextField(_('JavaScript'), blank=True, null=True,
            help_text=_('Extra JavaScript to inject into page, for example \
campaign tracking code (script tags must be included).'))

    def __unicode__(self):
        return _("SEO meta for %(path)s") % {'path': self.path_info}


class Analytic(models.Model):
    code = models.TextField(_('Code JavaScript'))
    description = models.CharField(_('Description'), max_length=250,
            blank=True, null=True, default='Main Analytic',
            help_text=_('An optional description used only for internal \
reference.'))
    is_active = models.BooleanField(_('Is active'), default=True)

    def __unicode__(self):
        regex = re.compile("('UA-.*')")
        try:
            return regex.findall(self.code)[0].replace("'", '')
        except:
            return _('Unknown analytic code')


class VirtualFile(models.Model):
    url = models.CharField(_('URL'), max_length=250, unique=True, db_index=True)
    content = models.TextField(_('File content'))
    is_active = models.BooleanField(_('Is active'), default=True)
    content_type = models.CharField(max_length=100,
                    choices=CONTENT_TYPE_CHOICES, default='text/plain')
    def save(self, *args, **kwargs):
        if self.url.startswith('/'):
            self.url = self.url[1:]
        super(VirtualFile, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.url
