import cv2, sys
from collections import deque
import numpy as np
import argparse
#import imutils
import urllib
import threading
from threading import Thread
from time import sleep
from send_bot import Main
from utils import printTimeDiff, initTimeDiff
from client import startListening, curFrame, frameFragments

#lower = {'Scorpion':(33, 23, 15), 'SubZero':(12, 27, 41)} #assign new item lower['blue'] = (93, 10, 0)
#upper = {'Scorpion':(97, 63, 32), 'SubZero':(87, 78, 84)}

boold = False

lower = {'Scorpion':(90, 0, 0), 'SubZero':(20, 31,42)} 
upper = {'Scorpion':(255, 255, 208), 'SubZero':(63, 88, 108)}

lowerhb = {'hb1':(60, 60, 60), 'hb2':(60,60,60)} #assign new item lower['blue'] = (93, 10, 0)
upperhb = {'hb1':(255, 255, 255), 'hb2':(255, 255, 255)}

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
        f = 131*(contrast + 127)/(127*(131-contrast))
        alpha_c = f
        gamma_c = 127*(1-f)

        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    return buf

t = None 
oldHealth1 = 3
oldHealth2 = 3

def example(frame):
    global t
    global oldHealth1
    global oldHealth2
    #TODO: do something with your frame
    damage1 = 0
    damage2 = 0
    orig_frame = frame
    circle1_x = "null"
    circle1_y = "null"

    circle2_x = "null"
    circle2_y = "null"
    hb1 = orig_frame[97:110,0:400]
    hb2 = orig_frame[97:110,400:800]

    hb1 = apply_brightness_contrast(hb1, 0, 50)
    hb2 = apply_brightness_contrast(hb2, 0, 50)

    #cv2.imshow("cs", hb1)
    #cv2.waitKey(1)

    key = "hb1"
    kernel = np.ones((9,9),np.uint8)
    mask = cv2.inRange(hb1, lowerhb[key], upperhb[key])
    #cv2.imshow("sc", mask)
    #cv2.waitKey(1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None


    mean1 = mask.mean()


    key = "hb2"
    kernel = np.ones((9,9),np.uint8)
    mask = cv2.inRange(hb2, lowerhb[key], upperhb[key])
    #cv2.imshow("ugff", mask)
    #cv2.waitKey(1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            
    # find contours in the mask and initialize the current
    # (x, y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    mean2 = mask.mean()

    if oldHealth1 - mean1 > 0.2:
        print("Took damage P1")
        damage1 = oldHealth1 - mean1
    oldHealth1 = mean1


    if oldHealth2 - mean2 > 0.2:
        print("Took damage P2")
        damage2 = oldHealth2 - mean2
    oldHealth2 = mean2
########################################




    frame_subZero =orig_frame
    frame_subZero = frame_subZero[250:-150,:]
    frame = frame[100:500,:]
    frame_scorpion = apply_brightness_contrast(frame, 0 ,73)
    #frame_scorpion = cv2.GaussianBlur(frame_scorpion, (11, 11), 0)
    #cv2.imshow("Da", frame_scorpion)
    
    #frame = apply_brightness_contrast(frame, 0 ,15);
    # blurred = cv2.GaussianBlur(frame, (11, 11), 0)

    #cv2.waitKey

    #for key, value in upper.items():
    key = "Scorpion"
    kernel = np.ones((9,9),np.uint8)
    mask = cv2.inRange(frame_scorpion, lower[key], upper[key])
    #cv2.imshow("da", mask)
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
        if radius > 0.1:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(orig_frame, (int(x), int(y)), int(radius), colors[key], 2)
            cv2.putText(orig_frame,key, (int(x-radius),int(y-radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,colors[key],2)
            circle1_x = x
            circle1_y = y

    key = "SubZero"
    kernel = np.ones((9,9),np.uint8)
    mask = cv2.inRange(frame_subZero, lower[key], upper[key])
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
        if radius > 0.08 and radius < 100:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(orig_frame, (int(x), int(y+200)), int(radius), colors[key], 2)
            cv2.putText(orig_frame,key, (int(x-radius),int(y-radius + 200)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,colors[key],2)
            circle2_x = x
            circle2_y = y
    
    # show the frame to our screen
    # f= open("../../guru99.txt","w+")
    # f.write(str(circle1_x) +' ' + str(circle1_y) + ' ' + str(circle2_x) + ' ' + str(circle2_y) + ' ' + str(mean1) + ' ' +str(mean2))
    # f.close()
    # print(mean1)
    data =[]

    if( (t is None) or (not t.isAlive())):
        data.append(str(circle1_x))
        data.append(str(circle1_y))
        data.append(str(circle2_x))
        data.append(str(circle2_y))
        data.append(str(mean1))
        data.append(str(mean2))
        data.append(damage1)
        data.append(damage2)

        t = threading.Thread(target = Main, args =[data])
        t.start()
    #render frame to our screen
    cv2.imshow('client', orig_frame)


    cv2.waitKey(1)



UDP_IP = "0.0.0.0"
UDP_PORT = 5005
if (len(sys.argv) > 1):
    UDP_PORT = int(sys.argv[1])
startListening(UDP_IP, UDP_PORT, example)
