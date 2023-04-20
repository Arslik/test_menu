from django.db import models
from django.urls import reverse


class Menu(models.Model):

    menu_title = models.CharField(max_length=15, verbose_name='Menu title')
    menu_slug = models.SlugField(max_length=255, default='', null=True, verbose_name='Menu slug')
    menu_url = models.CharField(max_length=255, verbose_name='Menu URL', blank=True)

    class Meta:
        name = 'Menu'

    def __str__(self):
        return self.menu_title

    def get_url(self):
        if self.menu_url:
            url = self.menu_url
        else:
            url = '/{}/'.format(self.menu_slug)
        return url


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='menu items', verbose_name='menu',
                             blank=True, null=True, on_delete=models.CASCADE)
    item_parent = models.ForeignKey('self', blank=True, null=True,
                                    related_name='menu items', verbose_name='parent menu item')
    item_title = models.CharField(max_length=20, verbose_name='Menu item title')
    item_url = models.CharField(max_length=255, verbose_name='Item Link', blank=True)
    item_named_url = models.CharField(max_length=255, verbose_name='Item URL', blank=True)

    class Meta:
        name = 'menu item'
        items_order = ('order', )

    def __str__(self):
        return self.item_title

    def get_url(self):
        if self.item_named_url:
            url = reverse(self.item_named_url)
        elif self.item_url:
            url = self.item_url
        else:
            url = '/'
        return url
