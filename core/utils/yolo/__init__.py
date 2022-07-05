import imp
from django.conf import settings

def get_classes():
    classes = []

    with open('core/utils/yolo/coco.names', 'r') as f:
        classes = f.read().splitlines()
    return classes