import cv2
import numpy as np
import io
from PIL import Image
import base64

def image_detection(a):
    img = a
    imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thrash = cv2.threshold(imgGry, 29, 255, cv2.CHAIN_APPROX_NONE)
    contours, hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    out = ""
    for contour in contours:
        
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        cv2.drawContours(img, [approx], 0, (255, 191, 0), 5)
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 5
        if len(approx) == 3:
            #cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 191, 0))
            
            out = "triangle"
            

        elif len(approx) == 4:
            #cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 191, 0))
            out = "square"
    

        elif len(approx) == 10:
            #cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 191, 0))
            out = "star"
        else:
            #cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 191, 0))
            out = "circle"

    # cv2.imshow('shapes', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    print(out)
    return out
