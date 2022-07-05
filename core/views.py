from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from core.utils.image_main import process_img


def deneme_view(r):
    # process_img()
    return HttpResponse('selam')


## TODO : ADD CSRF EXCEPT HERE
def upload_file_view(request):
    if request.method == 'POST':
        # name property that should be given should be image
        image = request.FILES.get('image')  
        if not image:
            return JsonResponse({
                "code": "error",
                "message": "Image should be provided"
            })
        return JsonResponse({
            "code": "success",
            "message": "yaşasın ırkımız çine bedel kırkımız",
        }) 
    return JsonResponse({
        "code": "error",
        "message": "only post requests are welcome",
    }) 
