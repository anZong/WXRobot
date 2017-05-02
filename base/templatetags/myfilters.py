from django import template
register = template.Library()


def split(value,arg):
    return [l for l in value.split(arg) if l]


def replace(value, arg):
    return value.replace(arg,'')

register.filter('split',split)
register.filter('replace',replace)
