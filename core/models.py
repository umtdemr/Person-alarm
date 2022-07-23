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
    distance_limit = models.PositiveIntegerField(blank=True, null=True)
    is_on = models.BooleanField(
        default=True,
        help_text="Control for processing img"
    )

    def __str__(self):
        return 'Site setting'


class ProcessedImage(models.Model):
    processed_image = models.ImageField(upload_to=processed_upload_directory)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class Image(models.Model):
    image = models.ImageField(upload_to=default_upload_directory)
    is_processed = models.BooleanField(default=False)
    related_img = models.OneToOneField(
        ProcessedImage,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.is_processed:
            return f'Processed {self.id}'
        return f'Default {self.id}'


class TelegramData(SingletonAbstract):
    """
    A model for sending data those from sensors
    """

    fire_info = models.BooleanField(default=False)

    def __str__(self):
        return f'Fire: {self.fire_info}'
 