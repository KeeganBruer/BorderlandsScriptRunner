import time
import win32api, ctypes
from Mouse import Mouse
class MouseMoveCommand:
    command = "MouseMove"
    def __init__(self):
        self.command = MouseMoveCommand.command
    def parse(self, line):
        lineSplit = line.split(" ")
        self.x= int(lineSplit[0].strip())
        self.y= int(lineSplit[1].strip())
        self.speed= lineSplit[2]
        if (len(lineSplit) > 3):
            self.isRelative = lineSplit[3].strip() == "R"
        else:
            self.isRelative = False
        return self
    def doCommand(self):
        Mouse().move_mouse_relative((self.x, self.y))
        #time.sleep(self.sleep_time / 1000)
    def __repr__(self):
        return "{} {} {} {} {}".format(self.command, self.x, self.y, self.speed, self.isRelative)
