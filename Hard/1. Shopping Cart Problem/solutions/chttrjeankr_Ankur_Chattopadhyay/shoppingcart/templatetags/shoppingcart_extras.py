from django import template

register = template.Library()


@register.filter
def get_quantity(cart, item_object):
    return cart.get(item_object, 0)
