import time

class EndCommand:
    command = "end"
    def __init__(self):
        self.command = EndCommand.command
        self.causeProgramToEnd = True
    def parse(self, line):
        return self
    def doCommand(self):
        pass
    def __repr__(self):
        return "{} {}".format(self.command, self.sleep_time)
