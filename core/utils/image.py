import cv2
import os
from io import BytesIO
from PIL import Image as PImage
from django.core.files.images import ImageFile

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
    writed, final_filename = process_img(image_obj)
    if writed:
        print('writed true')
        processed_img = PImage.open(f'media/{final_filename}')
        bytes_img = BytesIO()
        processed_img.save(bytes_img, 'JPEG')


        processed_obj = ProcessedImage.objects.create(
            processed_image=ImageFile(bytes_img, final_filename)
        )
        image_obj.related_img = processed_obj
        image_obj.save()
        print(f'Successfully created processed img: {processed_obj}')
        print('deleting temp image')
        os.remove(f'media/{final_filename}')


    ## TODO: process img
    return image_obj
