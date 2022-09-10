
import keyboard
import time
import pydirectinput

import json
from Commands.Command import Command
from OpencvUtils import getScreenshot
import cv2
from config import getConfig
from Commands.EndCommand import EndCommand
from Commands.SkipFileCommand import SkipFileCommand
    
def main():
    print("Loading configurations... Please wait ")
    time.sleep(2)
    scriptContent = loadScripts()
    interrupter = Interrupter(scriptContent)
    if (not waitForKeyPress()): return
    print("Starting script execution")
    time.sleep(2)
    

    
    interrupter.start()
    #



class Interrupter:
    def __init__(self, scriptContent):
        self.scriptContent = scriptContent
        self.screenshotName = 0
    def start(self):
        try:
            for fileLines in self.scriptContent:
                fileName = fileLines[0]
                print("Playing script: {}".format(fileName))
                for i in range(1, len(fileLines)):
                    line = fileLines[i]
                    line = ''.join([j if ord(j) < 128 else ' ' for j in line]) #Remove non unicode
                    splitLine = line.split("//") # remove comments
                    line = splitLine[0].replace("\r", "").replace("\n", "").strip() # Clear whitespace
                    if (line == ""): continue
                    
                    cmd = Command().parse(line.lower())
                    if (cmd == None): continue
                    print("Performing: {}".format(cmd))
                    if (cmd.command == EndCommand.command): return
                    if (cmd.command == SkipFileCommand.command): break
                    cmd.doCommand()
        except Exception as e:
            print(e.__traceback__.format_exc(), e)
            print("Press any key to close")
            charPressed = keyboard.read_key()
            return
        


def loadScripts():
    file_array = []
    files = getConfig("area_script_execution_order")
    for f in files:
        file_content = f+"\n"
        file_content += open("./AreaScripts/"+f, encoding='utf-8').read().strip()
        file_array.append(file_content.split("\n"))
    return file_array

def waitForKeyPress():
    print("Waiting for \"{}\" to be pressed, or \"{}\" to quit".format(
        getConfig("start_key").lower(), 
        getConfig("end_key").lower()
    ))
    while True:
        charPressed = keyboard.read_key()
        if (charPressed.lower() == getConfig("start_key").lower()):
            return True
        if (charPressed.lower() == getConfig("end_key").lower()):
            return False
    

if __name__ == "__main__":
    
    main()