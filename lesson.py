from time import *


class lesson:
    def __init__(self, name, unit, day, start, end):
        self.name = name
        self.day = day
        self.unit = unit
        self.start_time = start
        self.end_time = end
        self.formatted_start_time = self.format_time(start)
        self.formatted_end_time = self.format_time(end)

    def format_time(self, time):
        formated_time = time.hour + time.min / 60 - 8
        if self.day.lower() == "sun":
            formated_time += 10
        elif self.day.lower() == "mon":
            formated_time += 20
        elif self.day.lower() == "tue":
            formated_time += 30
        elif self.day.lower() == "wen":
            formated_time += 40
        return formated_time
