from django import template
register = template.Library()


def split(value,arg):
    return [l for l in value.split(arg) if l]

register.filter('split',split)