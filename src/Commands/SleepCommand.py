import time

class SleepCommand:
    command = "sleep"
    def __init__(self):
        self.command = SleepCommand.command
    def parse(self, line):
        self.sleep_time = int(line.strip())
        return self
    def doCommand(self):
        time.sleep(self.sleep_time / 1000)
    def __repr__(self):
        return "{} {}".format(self.command, self.sleep_time)
