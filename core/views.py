from django.http import HttpResponse
from django.shortcuts import render

from core.utils.image_main import process_img


def deneme_view(r):
    # process_img()
    return HttpResponse('selam')
