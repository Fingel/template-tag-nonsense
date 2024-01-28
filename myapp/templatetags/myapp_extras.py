from django import template

register = template.Library()


@register.simple_tag()
def bootstrap_alert(content):
    return "this is the custom tag: " + content


@register.simple_tag
def foo(val):
    return val.upper()
