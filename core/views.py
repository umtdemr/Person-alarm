from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from core.utils.image import create_default_image
from core.utils.image_main import process_img


def deneme_view(r):
    # process_img()
    return HttpResponse('selam')


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
        saved_img = create_default_image(image)
        return JsonResponse({
            "code": "success",
            "message": {
                "image": f'{settings.SITE_URL}{saved_img.image.url}'
            },
        }) 
    return JsonResponse({
        "code": "error",
        "message": "only post requests are welcome",
    }) 
