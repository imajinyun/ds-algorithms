import random


class Task:

    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getTimestamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitingTime(self, time):
        return time - self.timestamp
