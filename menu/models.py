from django.db import models


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
    menu = models.ForeignKey()