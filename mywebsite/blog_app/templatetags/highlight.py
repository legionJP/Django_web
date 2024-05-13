
from django import template
#from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter
def highligt_yellow(text, value): #search, #autoscape= True
    if text is  not None:
        text = str(text)
        src_str = re.compile(value,re.IGNORECASE)
        str_replaced = src_str.sub(f"<span class = \"highlight\">{value}</span>", text)
    else: 
        str_replaced = ''

    return mark_safe(str_replaced)        

    # if autosacpe:
    #     esc = conditional_escape
    # else:
    #     esc =lambda x:x 

    # result = re.sub(('%s') % re.escape(search), 
    #             '<span class = "highlight">%s</span>' %'\\1', esc(text)) 
    # return mark_safe(result)       


 
 # use this in the search.html fro highlight 

'''
 {% for result in results %} 
 <p>{{ result.title|highlight_yellow:query }}</p> 
 <p>{{ result.content|highlight_yellow:query}} </p> 
 <p> Author : {{ result.author|highlight_yellow:query}}</p> 
 {% endfor %}  
'''