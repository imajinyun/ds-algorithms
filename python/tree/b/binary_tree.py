class BinaryTree:
    """ 二叉树的节点与引用表示法 """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def getRootValue(self):
        return self.value

    def setRootValue(self, value):
        self.value = value

    def insertLeft(self, value):
        if self.left is None:
            self.left = BinaryTree(value)
        else:
            temp = BinaryTree(value)
            temp.left = self.left
            self.left = temp

    def insertRight(self, value):
        if self.right is None:
            self.right = BinaryTree(value)
        else:
            temp = BinaryTree(value)
            temp.right = self.right
            self.right = temp
