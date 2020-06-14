class BinaryTree:
    """
    二叉树的节点与引用表示法

    [理解二叉树的三种遍历](https://www.pianshen.com/article/7106254596/)
    """

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
            node = BinaryTree(value)
            node.left = self.left
            self.left = node

    def insertRight(self, value):
        if self.right is None:
            self.right = BinaryTree(value)
        else:
            temp = BinaryTree(value)
            temp.right = self.right
            self.right = temp

    def getTreeValues(self, tree):
        result, items, queue = [], [], []
        if tree is None:
            return items
        queue.append(tree)
        while queue:
            current = queue.pop(0)
            items.append(current)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        for item in items:
            result.append(item.getRootValue())
        return result

    def preOrder(self, items: list):
        """
        前序遍历（根左右）：在前序遍历中，先访问根节点，然后递归地前序遍历左子树，最后递归地前序遍历右子树。
        """
        items.append(self.getRootValue())
        if self.left:
            self.left.preOrder(items)
        if self.right:
            self.right.preOrder(items)

    def inOrder(self, items: list):
        """
        中序遍历（左根右）：在中序遍历中，先访问左子树，然后递归地中序遍历根节点，最后递归地中序遍历右子树。
        """
        if self.left:
            self.left.inOrder(items)
        items.append(self.getRootValue())
        if self.right:
            self.right.inOrder(items)

    def postOrder(self, items: list):
        """
        后序遍历（左右根）：在后序遍历中，先访问左子树，然后递归地前序遍历右子树，最后递归地后序遍历根节点。
        """
        if self.left:
            self.left.postOrder(items)
        if self.right:
            self.right.postOrder(items)
        items.append(self.getRootValue())
