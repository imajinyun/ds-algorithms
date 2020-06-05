class Queue:
    """ 使用列表模拟列表 """

    def __init__(self):
        self.items = []

    def isEmpty(self) -> bool:
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self) -> int:
        return len(self.items)
