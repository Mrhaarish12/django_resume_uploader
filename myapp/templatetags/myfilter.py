from django import template
register = template.Library()

def remove_chars(value,arg):
    for character in arg:
        value = value.replace(character,"")
    return value