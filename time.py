class time:
    def __init__(self, time):
        self.strtime = str(time)
        self.hour = 0
        self.min = 0
        self.convert()

    def convert(self):
        if ":" in self.strtime:
            self.hour, self.min = map(int, self.strtime.split(":"))
        else:
            self.hour = int(self.strtime)