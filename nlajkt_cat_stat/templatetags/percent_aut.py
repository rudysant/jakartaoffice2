from django import template

register = template.Library()

@register.filter
def as_percentage_of(part, whole):
    try:
        return "%.1f%%" % (float(part) / whole * 100)
    except (ValueError, ZeroDivisionError):
        return ""