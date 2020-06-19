class TreeNode:

    def __init__(self, key, value, left=None, right=None, parent=None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for node in self.left:
                    yield node
            yield self.key
            if self.hasRightChild():
                for node in self.right:
                    yield node

    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right

    def isLeftChild(self) -> bool:
        return self.parent and self.parent.left == self

    def isRightChild(self) -> bool:
        return self.parent and self.parent.right == self

    def isRoot(self) -> bool:
        return not self.parent

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
            self.left.parent = self
        if self.hasRightChild():
            self.right.parent = self

    def findSubNode(self):
        """
        查找后继节点：
          - 如果节点有右子节点，那么后继节点就是右子树中最小的节点；
          - 如果节点没有右子节点，并且其本身是父节点的左子节点，那么后继节点就是父节点；
          - 如果节点是父节点的右子节点，并且其本身没有右子节点，那么后继节点就是除其本身外父节点的后继节点；
        """
        node = None
        if self.hasRightChild():
            node = self.right.findMinNode()
        else:
            if self.parent:
                if self.isLeftChild():
                    node = self.parent
                else:
                    self.parent.right = None
                    node = self.parent.findSubNode()
                    self.parent.right = self
        return node

    def findMinNode(self):
        current = self
        while current.hasLeftChild():
            current = current.left
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
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
