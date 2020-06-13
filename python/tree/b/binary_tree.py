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

    def insertLeft(self, node):
        if self.left is None:
            self.left = BinaryTree(node)
        else:
            temp = BinaryTree(node)
            temp.left = self.left
            self.left = temp

    def insertRight(self, node):
        if self.right is None:
            self.right = BinaryTree(node)
        else:
            temp = BinaryTree(node)
            temp.left = self.left
            self.right = temp
