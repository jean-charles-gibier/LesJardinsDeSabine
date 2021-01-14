"""
trick picked from
https://stackoverflow.com/questions/49536060/best-way-to-introspect-an-object-in-django-templates"""
from django import template
import pprint

register = template.Library()

@register.simple_tag
def dirs(value):
    return str(pprint.pformat(value))