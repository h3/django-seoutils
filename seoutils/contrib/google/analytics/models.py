# -*- coding: utf-8 -*-

from django.db import models

SCRIPT_TEMPLATE = """
<script type="text/javascript">
var _gaq = _gaq || []; _gaq.push(['_setAccount', '%(code)s']); _gaq.push(['_trackPageview']);
(function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();
</script>
"""


class AnalyticCode(models.Model):
    code = models.CharField(max_length=25)
    note = models.CharField(max_length=25, blank=True, null=True)
    script = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def render(self):
        if self.script:
            return self.script
        else:
            return SCRIPT_TEMPLATE % {'code': self.code }

    def __unicode__(self):
        return u"Google Analytic code (%s)" % self.code

    class Meta:
        app_label = 'seoutils'
