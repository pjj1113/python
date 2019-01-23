from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.simple_tag
def pjj():
    return 123

@register.filter
def tyq(a,b):
    return a+b