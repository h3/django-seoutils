# -*- coding: utf-8 -*-

from django.db import models


class WebmastertoolsFile(models.Model):
    code = models.CharField(max_length=50, help_text='Example: google91c5ec673366c8b5.html')
    slug = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def render(self):
        return "google-site-verification: %s" % self.code

    def save(self, *args, **kwargs):
        self.code = self.code.strip()
        self.slug = self.code[6:-5]
        super(WebmastertoolsFile, self).save(*args, **kwargs)

    class Meta:
        app_label = 'seoutils'
