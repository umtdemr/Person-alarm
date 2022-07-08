import cv2


def cal_mid_point(pos):
    """
        Calculates middle point of rectangle
    """
    # find which point is bigger
    smaller_point = pos[1][1] if pos[0][1] > pos[1][1] else pos[0][1]
    # find middle point of rectange
    mid_point = int(smaller_point + abs(pos[0][1] - pos[1][1]) / 2)
    return mid_point

def calculate_line_mid_point(linePosition):
    x, y = 0, 0
    x = int(abs(linePosition[0][0] - linePosition[1][0]) / 2)
    y = int(abs(linePosition[0][1] - linePosition[1][1]) / 2)
    if linePosition[0][0] < linePosition[1][0]:
        x += linePosition[0][0]
    else:
        x += linePosition[1][0]
    
    if linePosition[0][1] < linePosition[1][1]:
        y += linePosition[0][1]
    else:
        y += linePosition[1][1]
    return (x, y)


def calculate_for_line(rect1Pos, rect2Pos):
    """
        Calculates line points that should be between two rectangles given.
    """
    
    # compare rectangles positions.
    if rect1Pos[1][0] < rect2Pos[0][0]:   # if target is on right
        return (
            (rect1Pos[1][0], cal_mid_point(rect1Pos)), # line start
            (rect2Pos[0][0], cal_mid_point(rect2Pos)) # line end
        )
    else:
        return (
            (rect1Pos[0][0], cal_mid_point(rect1Pos)), # line start
            (rect2Pos[1][0], cal_mid_point(rect2Pos)) # line end
        )

def get_normalized_distance(danger_area, target):
    """
        returns distance of centers of rectangles given
    """
    return int(cv2.norm(src1=danger_area, src2=target))

def get_color_for_distance(distance: int):
    if distance > 400:
        return (0, 255, 0)
    else:
        return (0, 0, 255)

def get_coordinates_for_text(img, found, settings_obj):
    location_x = settings_obj.image_width - 250
    location_y = int(settings_obj.image_height / 10) * found
    return (location_x, location_y)
