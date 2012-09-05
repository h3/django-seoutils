from seoutils.contrib.google.analytics.models import AnalyticCode
from django.utils.safestring import mark_safe

def script(request):
    out = []
    for code in AnalyticCode.objects.filter(is_active=True):
        out.append(code.render())
    return {
        'analytics_code': mark_safe(''.join(out)),
    }
