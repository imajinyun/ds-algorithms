class Stack:
    """ 将列表的头部作为栈的顶端 """

    def __init__(self):
        self.items = []

    def isEmpty(self) -> bool:
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)
