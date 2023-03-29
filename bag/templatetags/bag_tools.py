''' All of the strucutre, logic, functions and variable names are taken from
Code institute project
Boutique ado
https://github.com/Code-Institute-Solutions/boutique_ado_v1/
blob/250e2c2b8e43cccb56b4721cd8a8bd4de6686546/bag/templatetags/bag_tools.py'''
from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
