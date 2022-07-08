import cv2
import os
from io import BytesIO
from PIL import Image as PImage
from django.core.files.images import ImageFile
from django.conf import settings

from core.models import Image, ProcessedImage
from core.utils.image_main import process_img
from core.utils.tele_bot import TelegramBot


def read_img(path):
    return cv2.imread(path)

## TODO: switch process it default to true
def create_default_image(image, process_it=False) -> Image:
    """
        Creates image from provided image\n
        If process it set to true, process function runs and\n
        generates a processed image from given image
    """
    image_obj = Image.objects.create(
        image=image,
        is_processed=process_it
    )
    telegram_obj = TelegramBot()
    message = telegram_obj.send_photo(
        image_obj.image.url[1:],
        caption="motion captured"
    )
    
    if process_it:
        writed, final_filename = process_img(image_obj)
        if writed:
            # Open processed image for saving it to model
            processed_img = PImage.open(f'media/{final_filename}')
            bytes_img = BytesIO()
            processed_img.save(bytes_img, 'JPEG')

            # craete model from opened image
            processed_obj = ProcessedImage.objects.create(
                processed_image=ImageFile(bytes_img, final_filename)
            )

            # Edit default image for saying it has processed image
            image_obj.related_img = processed_obj
            image_obj.is_processed = True
            image_obj.save()

            telegram_obj.send_photo(
                processed_obj.processed_image.url[1:],
                reply_message_id=message.message_id,
                caption="processed image",
            )

            print(f'Successfully created processed img: {processed_obj}')
            print('deleting temp image')
            # delete unneccessary image cuz it is duplicated
            os.remove(f'media/{final_filename}')
            return image_obj, processed_obj
    return image_obj, None
