from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=200, verbose_name="название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "меню"
        verbose_name_plural = "меню"


class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name="меню",
                             related_name="items")

    name = models.CharField(max_length=200, verbose_name="название")
    level = models.PositiveIntegerField(verbose_name='уровень')
    parent = models.ForeignKey('Item', on_delete=models.CASCADE, verbose_name="родитель",
                               blank=True, null=True, related_name="children")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "пункт меню"
        verbose_name_plural = "пункты меню"
        ordering = ['level', 'name']
