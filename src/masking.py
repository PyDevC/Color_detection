import numpy as np
import cv2

def hsvmethod(frame, color):    
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    kernel = np.ones((5, 5), "uint8")
    if color.lower() == 'red':
        reddetect(frame, hsvFrame, kernel)
    elif color.lower() == 'blue':
        bluedetect(frame, hsvFrame, kernel)
    elif color.lower() == 'green':
        greendetect(frame, hsvFrame, kernel)
    elif color.lower() == 'all':
        all(frame, hsvFrame, kernel)
    
            
def reddetect(frame, hsvFrame, kernel):
    red_lower = np.array([0, 100, 100], np.uint8)
    red_upper = np.array([10, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

    red_mask = cv2.dilate(red_mask, kernel) 
    res_red = cv2.bitwise_and(frame, frame, mask = red_mask)

    contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
	
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv2.boundingRect(contour) 
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2) 
			
            cv2.putText(frame, "Red Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))
    
    
            
def greendetect(frame, hsvFrame, kernel):
    green_lower = np.array([25, 52, 72], np.uint8) 
    green_upper = np.array([102, 255, 255], np.uint8) 
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

    green_mask = cv2.dilate(green_mask, kernel) 
    res_green = cv2.bitwise_and(frame, frame, mask = green_mask) 

    contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
	
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv2.boundingRect(contour) 
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) 
			
            cv2.putText(frame, "Green Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0)) 


def bluedetect(frame, hsvFrame, kernel):
    blue_lower = np.array([94, 80, 2], np.uint8) 
    blue_upper = np.array([120, 255, 255], np.uint8) 
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

    blue_mask = cv2.dilate(blue_mask, kernel) 
    res_blue = cv2.bitwise_and(frame, frame, mask = blue_mask) 

    contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv2.boundingRect(contour) 
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) 
			
            cv2.putText(frame, "Blue Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0)) 

def all(frame, hsvFrame, kernel):
    reddetect(frame, hsvFrame, kernel)
    bluedetect(frame, hsvFrame, kernel)
    greendetect(frame, hsvFrame, kernel)