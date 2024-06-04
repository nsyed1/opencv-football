def get_center_of_bbox(bbox):
    x1, y1, x2, y2 = bbox

    return int((x1+x2)/2), int((y1+y2)/2)

def get_bbox_width(bbox):
    x1 = bbox[0]
    x2 = bbox[2]
    return x2-x1