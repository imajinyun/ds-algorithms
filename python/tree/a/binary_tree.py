class BinaryTree:
    """ 二叉树的列表之列表表示法 """

    @staticmethod
    def getTree(value=0) -> list:
        return [value, [], []]

    @staticmethod
    def getRootValue(root: list):
        return root[0]

    @staticmethod
    def setRootValue(node, value) -> None:
        node[0] = value

    @staticmethod
    def getLeftChild(root: list) -> list:
        return root[1]

    @staticmethod
    def getRightChild(root: list) -> list:
        return root[2]

    @staticmethod
    def insertLeft(root: list, branch) -> list:
        left = root.pop(1)
        if len(left) > 1:
            root.insert(1, [branch, left, []])
        else:
            root.insert(1, [branch, [], []])
        return root

    @staticmethod
    def insertRight(root, branch) -> list:
        right = root.pop(2)
        if len(right) > 1:
            root.insert(2, [branch, [], right])
        else:
            root.insert(2, [branch, [], []])
        return root
