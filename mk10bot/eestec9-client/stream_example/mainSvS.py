import cv2, sys
from collections import deque
import numpy as np
import argparse
#import imutils
import urllib


from utils import printTimeDiff, initTimeDiff
from client import startListening, curFrame, frameFragments

#lower = {'Scorpion':(33, 23, 15), 'SubZero':(12, 27, 41)} #assign new item lower['blue'] = (93, 10, 0)
#upper = {'Scorpion':(97, 63, 32), 'SubZero':(87, 78, 84)}

lower = {'Scorpion':(38, 0, 0), 'SubZero':(48, 0, 0)} 
upper = {'Scorpion':(255, 255, 255), 'SubZero':(185, 200, 200)}

colors = {'Scorpion':(0,0,255), 'SubZero':(0,255,0)}

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
    #orig_frame[100:-50,:] = [0,0,0]
    orig_frame = orig_frame[150:-120,:]
    #orig_frame = cv2.cvtColor(orig_frame, cv2.COLOR_BGR2HSV)
    #orig_frame = cv2.GaussianBlur(orig_frame, (15, 15), 0)
    frame_sz = orig_frame[:,:]
    frame_scorpion = apply_brightness_contrast(orig_frame, 0 ,0)
    frame_scorpion = cv2.GaussianBlur(frame_scorpion, (11, 11), 0)
    
    frame_sz = apply_brightness_contrast(frame_sz, 0 ,30); #85 105
    #frame_sz = cv2.GaussianBlur(frame_sz, (7, 7), 0)
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #cv2.imshow("lal", frame_sz)

    #cv2.waitKey

    #for key, value in upper.items():
    key = "Scorpion"
    kernel = np.ones((9,9),np.uint8)
    mask = cv2.inRange(frame_scorpion, lower[key], upper[key])
    #cv2.imshow("sc", frame_scorpion)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            
    # find contours in the mask and initialize the current
    # (x, y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None


    
    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    
        # only proceed if the radius meets a minimum size. Correct this value for your obect's size
        if radius > 5:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(orig_frame, (int(x), int(y)), int(radius), colors[key], 2)
            cv2.putText(orig_frame,key, (int(x-radius),int(y-radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,colors[key],2)
            #frame_sz[(int)(y-500):(int)(y+500),(int)(x-200):(int)(x+200)] = [0,0,0]
            #orig_frame[(int)(y-200):(int)(y+200),(int)(x-100):(int)(x+100)] = [0,0,0]


    #frame_sz[(int)(y-200):(int)(y+200),(int)(x-100):(int)(x+100)] = [0,0,0]

    #cv2.imshow("ghh", frame_sz)
    key = "SubZero"
    kernel = np.ones((9,9),np.uint8)
    frame_sz[(int)(y-500):(int)(y+500),(int)(x-100):(int)(x+100)] = [0,0,0]
    mask = cv2.inRange(frame_sz, lower[key], upper[key])
    #cv2.imshow("ugff", mask)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            
    # find contours in the mask and initialize the current
    # (x, y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    
        # only proceed if the radius meets a minimum size. Correct this value for your obect's size
        if radius > 5:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(orig_frame, (int(x), int(y + 0)), int(radius), colors[key], 2)
            cv2.putText(orig_frame,key, (int(x-radius),int(y-radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,colors[key],2)

                    
    # show the frame to our screen

    #render frame to our screen
    cv2.imshow('client', orig_frame)
    cv2.waitKey(1)


UDP_IP = "0.0.0.0"
UDP_PORT = 5005
if (len(sys.argv) > 1):
    UDP_PORT = int(sys.argv[1])
startListening(UDP_IP, UDP_PORT, example)
