import numpy as np
import cv2
import pyautogui
from direct_inputs import PressKey, ReleaseKey 
from KeyCodes import keyStringToVirtualCode
from OpencvUtils import moveMouseToCenterOfImageOnScreen
import time
from config import getConfig

VK_RIGHT = keyStringToVirtualCode("right")
VK_LEFT = keyStringToVirtualCode("left")

class LookAtCommand:
    command = "lookAt"
    def __init__(self):
        self.command = LookAtCommand.command
    def parse(self, line):
        splitLine = line.split(" ")
        self.filename = splitLine[0].strip()
        if (len(splitLine) > 1):
            self.tolerance = int(splitLine[1].strip())
        else:
            self.tolerance = getConfig("default_look_tolerance")
        self.filelocation = './Images/'+self.filename
        self.image = cv2.imread(self.filelocation)
        self.image = cv2.cvtColor(self.image,
                        cv2.COLOR_RGB2BGR)
        return self
    def doCommand(self):
        moveMouseToCenterOfImageOnScreen(self.image, [int(self.tolerance/2)*-1, int(self.tolerance/2)])
    def __repr__(self):
        return "{} {}".format(self.command, self.filelocation)





