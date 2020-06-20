class TreeNode:

    def __init__(self, key, value, left=None, right=None, parent=None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.balanceFactor = 0

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for node in self.left:
                    yield node
            yield self.key
            if self.hasRightChild():
                for node in self.right:
                    yield node

    def hasLeftChild(self) -> bool:
        return self.left is not None

    def hasRightChild(self) -> bool:
        return self.right is not None

    def isLeftChild(self) -> bool:
        return self.parent and self.parent.left == self

    def isRightChild(self) -> bool:
        return self.parent and self.parent.right == self

    def isRoot(self):
        return self.parent is None

    def isLeaf(self):
        return not (self.left or self.right)

    def hasAnyChildren(self):
        return self.left or self.right

    def hasBothChildren(self):
        return self.left and self.right

    def replace(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        if self.hasLeftChild():
            self.parent.left = left
        if self.hasRightChild():
            self.parent.right = right

    def findSubNode(self):
        node = None
        if self.hasRightChild():
            node = self.right.findMinNode()
        else:
            if self.parent:
                if self.hasLeftChild():
                    node = self.parent
                else:
                    self.parent.right = None
                    node = self.parent.findMinNode()
                    self.parent.right = self
        return node

    def findMinNode(self):
        current = self
        while current.hasLeftChild():
            current = current.left
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.hasLeftChild():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent
