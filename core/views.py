from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from core.utils.image import create_default_image
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
                "message": "Image should be provided"
            })
        saved_img, processed_img = create_default_image(image)
        return JsonResponse({
            "code": "success",
            "message": {
                "image": f'{settings.SITE_URL}{saved_img.image.url}',
                "processed_img": f'{settings.SITE_URL}{processed_img.processed_image.url}' if processed_img else '',
            },
        }) 
    return JsonResponse({
        "code": "error",
        "message": "only post requests are welcome",
    }) 
