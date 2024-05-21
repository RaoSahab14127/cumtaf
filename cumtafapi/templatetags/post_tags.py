from django import template
from django.contrib.auth.models import User
from datetime import datetime
register = template.Library()

def total_tu(value, elements):
    return  value[:len(value)-elements]

register.filter("total_tu",total_tu)
@register.simple_tag
def total():
    return  "date"


