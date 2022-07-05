from django.db import models

from core.abstract_models import SingletonAbstract
from core.utils.file import (
    processed_upload_directory, 
    default_upload_directory
)


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


class ProcessedImage(models.Model):
    processed_image = models.ImageField(upload_to=processed_upload_directory)
    created_at = models.DateTimeField(auto_now=True)


class Image(models.Model):
    image = models.ImageField(upload_to=default_upload_directory)
    related_img = models.OneToOneField(
        ProcessedImage,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.is_processed:
            return f'Processed {self.id}'
        return f'Default {self.id}'
