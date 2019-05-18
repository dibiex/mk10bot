import cv2, sys
from collections import deque
import numpy as np
import argparse
#import imutils
import urllib



from utils import printTimeDiff, initTimeDiff
from client import startListening, curFrame, frameFragments

lower = {'hb1':(60, 60, 60), 'hb2':(60,60,60)} #assign new item lower['blue'] = (93, 10, 0)
upper = {'hb1':(255, 255, 255), 'hb2':(255, 255, 255)}


def apply_brightness_contrast(input_img, brightness = 0, contrast = 0):

    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow)/255
        gamma_b = shadow

        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()

    if contrast != 0:
        f = float(131*(contrast + 127))/(127*(131-contrast))
        alpha_c = f
        gamma_c = 127*(1-f)

        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    return buf

def example(frame):
    #TODO: do something with your frame
    orig_frame = frame
    
    hb1 = orig_frame[97:110,0:400]
    hb2 = orig_frame[97:110,400:800]

    hb1 = apply_brightness_contrast(hb1, 0, 50)
    hb2 = apply_brightness_contrast(hb2, 0, 50)

    #cv2.imshow("cs", hb1)
    #cv2.waitKey(1)

    key = "hb1"
    kernel = np.ones((9,9),np.uint8)
    mask = cv2.inRange(hb1, lower[key], upper[key])
    #cv2.imshow("sc", mask)
    #cv2.waitKey(1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None


    mean1 = mask.mean()
    print(mean1)


    key = "hb2"
    kernel = np.ones((9,9),np.uint8)
    mask = cv2.inRange(hb2, lower[key], upper[key])
    cv2.imshow("ugff", mask)
    cv2.waitKey(1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            
    # find contours in the mask and initialize the current
    # (x, y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    mean2 = mask.mean()
    # show the frame to our screen

    #render frame to our screen
    cv2.imshow('client', orig_frame)
    cv2.waitKey(1)


UDP_IP = "0.0.0.0"
UDP_PORT = 5005
if (len(sys.argv) > 1):
    UDP_PORT = int(sys.argv[1])
startListening(UDP_IP, UDP_PORT, example)
