import os
import cv2
import numpy as np
from django.conf import settings

from core.utils.image import read_img
from core.utils.yolo import get_classes
from core.utils import (
    get_normalized_distance,
    calculate_for_line, 
    get_coordinates_for_text, 
)

def process_img():
    weight_path = 'core/utils/yolo/yolov3.weights'
    cfg_path = 'core/utils/yolo/yolov3.cfg'
    img_path = 'media/me.jpeg'
    yolo = cv2.dnn.readNet(weight_path, cfg_path)

    classes = get_classes()

    # read img
    img = read_img(img_path)

    # danger area
    fstart_point = (80, 10)
    fend_point = (300, 400)
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
        color = colors[i]
        box = boxes[i]

        # if the recognized object is person, draw line
        if class_ids[i] == 0:
            line_positions = calculate_for_line((fstart_point, fend_point), ((x,y), (x+w, y+h)))
            line = cv2.line(img, line_positions[0], line_positions[1], color, 4
            )
            
            # get distance between two points of line
            distance = cv2.norm(src1=line_positions[0], src2=line_positions[1])
            if class_id == 0: 
                found += 1
            # put text to 
            cv2.putText(
                line, 
                f'd={get_normalized_distance(line_positions[0], line_positions[1])}',
                get_coordinates_for_text(img, found),
                cv2.FONT_HERSHEY_SIMPLEX,
                2,
                color,
                5
            )

        cv2.rectangle(img, (x, y), (x+w, y+h), color, 4)
        cv2.putText(img, f'%{confi_percent} {label}', (x, y - 10), font, 3, (255, 255, 255), 4)


    writed = cv2.imwrite('media/deneme.jpeg', img)
    return writed
