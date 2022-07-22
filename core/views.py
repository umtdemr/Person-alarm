from time import sleep
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.images import ImageFile
from django.conf import settings

from core.utils.image import capture_photo, create_default_image
from core.utils.image_main import process_img


def home_view(_):
    # process_img()
    return JsonResponse({
        "code": "info",
        "message": "app is running. waiting for images..."
    })


@csrf_exempt
def upload_file_view(request):
    if request.method == 'POST':
        # name property that should be given should be image
        image = request.FILES.get('image')  
        if not image:
            return JsonResponse({
                "code": "error",
                "limit": False,
                "message": "Image should be provided"
            })
        saved_img, processed_img, limit = create_default_image(image)
        return JsonResponse({
            "code": "success",
            "limit": limit,
            "message": {
                "image": f'{settings.SITE_URL}{saved_img.image.url}',
                "processed_img": f'{settings.SITE_URL}{processed_img.processed_image.url}' if processed_img else '',
            },
        }) 
    return JsonResponse({
        "code": "error",
        "limit": False,
        "message": "only post requests are welcome",
    }) 


@csrf_exempt
def capture_photo_view(request):
    if request.method == "POST":
        writed = capture_photo()
        if writed:
            captured_image_file = open('media/captue.jpeg', 'rb')
            captured_image = ImageFile(captured_image_file)
            saved_img, processed_img = create_default_image(captured_image)
            return JsonResponse({
                "captured": writed,
                "image": f'{settings.SITE_URL}{saved_img.image.url}',
                "processed_img": f'{settings.SITE_URL}{processed_img.processed_image.url}' if processed_img else '',
            })
        return JsonResponse({
            "captured": writed
        })
