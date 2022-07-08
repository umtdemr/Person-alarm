import os
import uuid
import cv2
import numpy as np

from core.models import SiteSettings
from core.utils.yolo import get_classes
from core.utils import (
    get_normalized_distance,
    calculate_for_line, 
    get_coordinates_for_text, 
)

def get_danger_area():
    """ get danger are points from SiteSettings """
    settings_obj = SiteSettings.objects.first()
    x = settings_obj.rect_x
    y = settings_obj.rect_y
    w = x + settings_obj.rect_w
    h = y + settings_obj.rect_h
    return (x, y), (w, h)


# TODO: generate danger area from settings obj
def process_img(image_obj):
    """
        Run yolov3 algorithm for recognizing persons and \n
        calculating `their distance` from danger area
    """
    settings_obj = SiteSettings.objects.first()
    is_limit_exceeded = False
    print(image_obj.image.url)
    print(os.getcwd())
    weight_path = 'core/utils/yolo/yolov3.weights'
    cfg_path = 'core/utils/yolo/yolov3.cfg'
    img_path = image_obj.image.url[1:] # getting the image url without the first backslash
    print(weight_path)
    print(cfg_path)
    print(img_path)
    yolo = cv2.dnn.readNet(weight_path, cfg_path)

    classes = get_classes()

    # read img
    img = cv2.imread(img_path)

    # danger area
    fstart_point, fend_point = get_danger_area()
    rect_danger = cv2.rectangle(img, fstart_point, fend_point, (0, 0, 255), -1)

    # yolo algorithm
    blob = cv2.dnn.blobFromImage(img, 1/255, (320, 320), (0, 0, 0), swapRB=True, crop=False)

    yolo.setInput(blob)
    output_layes_name = yolo.getUnconnectedOutLayersNames()
    layeroutput = yolo.forward(output_layes_name)

    boxes = []
    confidences = []
    class_ids = []
    width = img.shape[1]
    height = img.shape[0]


    found = 0

    for output in layeroutput:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.7:
                center_x = int(detection[0]*width)
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x,y,w,h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(len(boxes), 3))


    for i in indexes.flatten():
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        confi = str(round(confidences[i], 2))
        confi_percent = int(confidences[i] * 100)
        print(confi_percent)
        color = colors[i]
        box = boxes[i]

        # if the recognized object is person, draw line
        if class_ids[i] == 0:
            line_positions = calculate_for_line((fstart_point, fend_point), ((x,y), (x+w, y+h)))
            line = cv2.line(img, line_positions[0], line_positions[1], color, 4
            )
            
            # get distance between two points of line
            distance = cv2.norm(src1=line_positions[0], src2=line_positions[1])
            if distance <= settings_obj.distance_limit:
                is_limit_exceeded = True
            if class_id == 0: 
                found += 1
            # put text to 
            cv2.putText(
                line, 
                f'd={get_normalized_distance(line_positions[0], line_positions[1])}',
                get_coordinates_for_text(img, found, settings_obj),
                cv2.FONT_HERSHEY_SIMPLEX,
                2,
                color,
                4
            )

        cv2.rectangle(img, (x, y), (x+w, y+h), color, 4)
        cv2.putText(img, f'%{confi_percent} {label}', (x, y - 10), font, 3, (255, 255, 255), 4)

    final_filename = f'{str(uuid.uuid4()).replace("-", "")}.jpeg'
    writed = cv2.imwrite(f'media/{final_filename}', img)
    print(writed)
    return writed, final_filename, is_limit_exceeded
