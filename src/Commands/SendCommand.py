from KeyCodes import keyStringToVirtualCode
from direct_inputs import PressKey, ReleaseKey 
import time

class SendCommand:
    command = "send"
    def __init__(self):
        self.command = SendCommand.command
        self.sendArray = []

    def parse(self, line):
        inBrace = False
        curr = ""
        sendArray = []
        for c in line:
            if (c == "{"):
                inBrace = True
            elif (c == "}"):
                inBrace = False
                sendArray.append(curr)
                curr = ""
            elif (inBrace):
                curr += c
            else:
                sendArray.append(c)
        sendArray = [x.strip() for x in sendArray]
        sendArray = filter(lambda x : x != "", sendArray)
        for item in sendArray:
            splitItem = item.split(" ")
            if (len(splitItem) > 1):
                self.sendArray.append(splitItem)
            else:
                self.sendArray.append([splitItem[0], "down"])
                self.sendArray.append([splitItem[0], "up"])
        return self
    def doCommand(self):
        for send in self.sendArray:
            keyCode = keyStringToVirtualCode(send[0])
            if (send[1] == "down"):
                PressKey(keyCode)
            else:
                ReleaseKey(keyCode)
            time.sleep(0.01)
    def __repr__(self):
        return "{} {}".format(self.command, "".join(["{"+x[0]+" "+x[1]+"}" for x in self.sendArray]))
