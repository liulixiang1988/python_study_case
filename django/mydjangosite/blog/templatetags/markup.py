#-*- coding:utf-8 -*-
from django.conf import settings
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

__author__ = 'liulixiang'

from django import template


register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def markdown2(value):
    try:
        import markdown2
    except ImportError:
        if settings.DEBUG:
            raise template.TemplateSyntaxError("Error in 'markdown2' filter: The Markdown2 isn't installed")
        return force_text(value)
    else:
        return mark_safe(markdown2.markdown(force_text(value), safe_mode=True, extras=["code-friendly", ]))


