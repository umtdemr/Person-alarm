from concurrent.futures import process
from typing import TYPE_CHECKING
import cv2

from core.models import Image, ProcessedImage
from core.utils.image_main import process_img


def read_img(path):
    return cv2.imread(path)

## TODO: switch process it default to true
def create_default_image(image, process_it=False) -> Image:
    """
        Creates image from provided image\n
        If process it set to true, process function runs
    """
    image_obj = Image.objects.create(
        image=image,
        is_processed=process_it
    )
    process_img(image_obj)

    ## TODO: process img
    return image_obj
