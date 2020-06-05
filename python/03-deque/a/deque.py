class Deque:
    """ 双端队列 """

    def __init__(self):
        self.items = []

    def isEmpty(self) -> bool:
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self) -> int:
        return len(self.items)
