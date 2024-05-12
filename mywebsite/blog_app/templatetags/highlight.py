
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter(needs_autoescape=True)
def highligt(text, search ,autosacpe= True):
    if autosacpe:
        esc = conditional_escape
    else:
        esc =lambda x:x 

    result = re.sub(('%s') % re.escape(search), 
                '<span class = "highlight">%s</span>' %'\\1', esc(text)) 
    return mark_safe(result)       

