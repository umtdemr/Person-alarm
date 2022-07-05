from django.db import models

from core.abstract_models import SingletonAbstract

class SiteSettings(SingletonAbstract):
    rect_x = models.PositiveIntegerField(blank=True, null=True)
    rect_y = models.PositiveIntegerField(blank=True, null=True)
    rect_w = models.PositiveIntegerField(blank=True, null=True)
    rect_h = models.PositiveIntegerField(blank=True, null=True)
    image_width = models.PositiveIntegerField(blank=True, null=True)
    image_height = models.PositiveIntegerField(blank=True, null=True)
    resize = models.BooleanField(default=False)
    resize_width = models.PositiveIntegerField(blank=True, null=True)
    resize_height = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return 'Site setting'
