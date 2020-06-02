class Stack:
    """将列表的尾部作为栈的顶端"""

    def __init__(self):
        self.items = []

    def isEmpty(self) -> bool:
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self) -> int:
        return len(self.items)
