from Commands.SendCommand import SendCommand
from Commands.SleepCommand import SleepCommand
from Commands.LookAtCommand import LookAtCommand
from Commands.MouseMoveCommand import MouseMoveCommand
from Commands.EndCommand import EndCommand
from Commands.SkipFileCommand import SkipFileCommand

class Command:
    def __init__(self):
        pass
    def parse(self, line):
        lineWords = line.split(" ")
        self.command = lineWords[0]
        commandEvent = None
        print(self.command, lineWords)
        if (self.command == SendCommand.command.lower()):
            commandEvent = SendCommand().parse(line.replace(self.command, "").strip())
        elif (self.command == SleepCommand.command.lower()):
            commandEvent = SleepCommand().parse(line.replace(self.command, "").strip())
        elif (self.command == LookAtCommand.command.lower()):
            commandEvent = LookAtCommand().parse(line.replace(self.command, "").strip())
        elif (self.command == MouseMoveCommand.command.lower()):
            commandEvent = MouseMoveCommand().parse(line.replace(self.command, "").strip())
        elif (self.command == SkipFileCommand.command.lower()):
            commandEvent = SkipFileCommand().parse(line.replace(self.command, "").strip())
        
        if (not commandEvent == None):
            commandEvent.causeProgramToEnd = False

        if (self.command == EndCommand.command.lower()):
            commandEvent = EndCommand().parse(line.replace(self.command, "").strip())
        
        return commandEvent

    def __repr__(self):
        return "{}".format(self.command)
