from a.node import Node


class Ordered:
    """ 有序链表 """

    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        s = ''
        if self.size() == 0:
            return s
        curr = self.head
        while curr is not None:
            s += str(curr.getData()) + '->'
            curr = curr.getNext()
        return s.rstrip('->')

    def isEmpty(self) -> bool:
        return self.head is None

    def add(self, item):
        prev, curr, stop = None, self.head, False
        while curr is not None and not stop:
            if curr.getData() > item:
                stop = True
            else:
                prev = curr
                curr = curr.getNext()

        node = Node(item)
        if prev is None:
            node.setNext(self.head)
            self.head = node
        else:
            node.setNext(curr)
            prev.setNext(node)

    def remove(self, item):
        prev, curr, found = None, self.head, False
        while curr is not None and not found:
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
        curr, found, stop = self.head, False, False
        while curr is not None and not found and not stop:
            if curr.getData() == item:
                found = True
            else:
                if curr.getData() > item:
                    stop = True
                else:
                    curr = curr.getNext()
        return found

    def index(self, item) -> int:
        curr, found, stop, index = self.head, False, False, 0
        while curr is not None and not found and not stop:
            index += 1
            if curr.getData() == item:
                found = True
            else:
                if curr.getData() > item:
                    stop = True
                else:
                    curr = curr.getNext()
        return index

    def size(self) -> int:
        curr, count = self.head, 0
        while curr is not None:
            count += 1
            curr = curr.getNext()
        return count
