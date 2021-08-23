from django import template

register = template.Library()


@register.filter
def filter_multi(x,y):
    return x * y
