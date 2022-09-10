import time

class SkipFileCommand:
    command = "skipFile"
    def __init__(self):
        self.command = SkipFileCommand.command
    def parse(self, line):
        return self
    def doCommand(self):
        pass
    def __repr__(self):
        return "skip file"
