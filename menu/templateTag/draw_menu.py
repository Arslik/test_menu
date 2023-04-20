from django import template
from menu.models import Menu
from django.db.models import Prefetch

register = template.Library()
# menu = Prefetch('items__items__items__items')

def draw_menu(context, menu_slug) -> dict:
    try:
        menu = Menu.objects.prefetch_related('items__items__items__items').get(slug=menu_slug)
        return {'menu': menu, 'context':context}
    except Menu.DoesNotExist:
        return {'menu': '', 'context': context}