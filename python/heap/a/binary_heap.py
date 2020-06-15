class BinaryHeap:

    def __init__(self) -> None:
        self.heap = [0]
        self.count = 0

    def isEmpty(self) -> bool:
        return self.count == 0

    def size(self) -> int:
        return self.count

    def insert(self, value) -> None:
        self.heap.append(value)
        self.count += 1
        self.siftUp(self.count)

    def delMinElement(self):
        result = self.heap[1]
        self.heap[1] = self.heap[self.count]
        self.count -= 1
        self.heap.pop()
        self.siftUp(1)
        return result

    def buildHeap(self, items) -> None:
        i = len(items) // 2
        self.count = len(items)
        self.heap = [0] + items[:]
        while i > 0:
            self.siftDown(i)
            i -= 1

    def siftUp(self, i) -> None:
        """
        对于完全二叉树，对于在列表中处于位置 p 的节点来说，它的左子节点正好处于位置 2p；同理，右子节点处于位置 2p+1
        """
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

    def siftDown(self, i) -> None:
        while i * 2 <= self.count:
            j = self.getMinIndex(i)
            if self.heap[i] > self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def getMinIndex(self, i) -> int:
        if i * 2 + 1 > self.count:
            return i * 2
        else:
            return i * 2 if self.heap[i * 2] < self.heap[i * 2 + 1] else i * 2 + 1
