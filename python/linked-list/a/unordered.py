from a.node import Node


class Unordered:
    """ 无序链表 """

    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        if self.size() == 0:
            return ''
        s = ''
        curr = self.head
        while curr is not None:
            s += str(curr.getData()) + '->'
            curr = curr.getNext()
        return s.rstrip('->')

    def isEmpty(self) -> bool:
        return self.head is None

    def add(self, item):
        node = Node(item)
        node.setNext(self.head)
        self.head = node

    def remove(self, item):
        curr, prev, found = self.head, None, False
        while not found:
            if curr.getData() == item:
                found = True
            else:
                prev = curr
                curr = curr.getNext()

        if prev is None:
            self.head = curr.getNext()
        else:
            prev.setNext(curr.getNext())

    def search(self, item) -> bool:
        curr, found = self.head, False
        while curr is not None and not found:
            if curr.getData() == item:
                found = True
            else:
                curr = curr.getNext()
        return found

    def index(self, item) -> int:
        curr, found, index = self.head, False, 0
        while curr is not None and not found:
            index += 1
            if curr.getData == item:
                found = True
            curr = curr.getNext()

        return index

    def size(self):
        curr, count = self.head, 0
        while curr is not None:
            count += 1
            curr = curr.getNext()
        return count
