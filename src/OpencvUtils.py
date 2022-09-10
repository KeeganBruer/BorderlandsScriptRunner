import cv2, pyautogui
import numpy as np
from direct_inputs import PressKey, ReleaseKey 
from KeyCodes import keyStringToVirtualCode
from Mouse import Mouse
import time
import os
import glob
VK_RIGHT = keyStringToVirtualCode("right")
VK_LEFT = keyStringToVirtualCode("left")

def drawRectOnImage(rect, image):
    # Step 3: Draw the rectangle on large_image
    cv2.rectangle(image, (rect[0],rect[1]),(rect[1]+rect[2],rect[1]+rect[3]),(0,0,255),2)
    return image
def drawRectAndShow(rect, image):
    # Step 3: Draw the rectangle on large_image
    image = drawRectOnImage(rect, image)
    # Display the original image with the rectangle around the match.
    cv2.imshow('output',image)

    # The image is only displayed if we call this
    cv2.waitKey(0)
def getScreenshot():
    # take screenshot using pyautogui
    screenshot = pyautogui.screenshot()
    
    # since the pyautogui takes as a 
    # PIL(pillow) and in RGB we need to 
    # convert it to numpy array and BGR 
    # so we can write it to the disk
    screenshot = cv2.cvtColor(np.array(screenshot),
                        cv2.COLOR_RGB2BGR)

    large_image = cv2.imread('./Images/SSh_full.png')
    return screenshot

def getRectFromImages(small_image, large_image):
    method = cv2.TM_SQDIFF_NORMED
    result = cv2.matchTemplate(small_image, large_image, method)

    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    # Draw the rectangle:
    # Extract the coordinates of our best match
    MPx,MPy = mnLoc
    print("X ",MPx, " Y ",MPy)

    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = small_image.shape[:2]

    return [MPx, MPy, tcols, trows]

def getDifferenceFromCenter(rect_array, screenshot):
    [box_x, box_y, box_width, box_height] = rect_array
    screen_height,screen_width = screenshot.shape[:2]
    
    center_box_x = box_x + (box_width / 2)
    center_box_y = box_y + (box_height / 2)
    #print("box center ", center_box_x, center_box_y)

    screen_center_x = screen_width / 2
    screen_center_y = screen_height / 2
    #print("screen center ", screen_center_x, screen_center_y)

    dist_x = center_box_x - screen_center_x
    dist_y = center_box_y - screen_center_y
    print("dist ", dist_x, dist_y)

    return [dist_x, dist_y]

def moveMouseToCenterOfImageOnScreen(small_image, tolerance_range):
    screenshotName = 0
    # Create or clear screenshot directory
    if not os.path.exists("./Screenshots/"):
        os.makedirs("./Screenshots/")
    else:
        files = glob.glob('./Screenshots/*')
        for f in files:
            os.remove(f)

    while True:
        large_image = getScreenshot()
        rect = getRectFromImages(small_image, large_image)
        pos = getDifferenceFromCenter(rect, large_image)
        
        if (pos[0] > tolerance_range[0]):
            Mouse().move_mouse_relative((-10, 0))
        if (pos[0] < tolerance_range[1]):
            Mouse().move_mouse_relative((10, 0))
        else:
            break

        rect = getRectFromImages(small_image, large_image)
        drawRectOnImage(rect, large_image)
        cv2.imwrite("./Screenshots/"+str(screenshotName)+".png", large_image)
        screenshotName += 1
    files = glob.glob('./Screenshots/*')
    for f in files:
        os.remove(f)
    os.rmdir('./Screenshots/')

