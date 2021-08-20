from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def filter_multi(x,y):
    return x * y
