import unittest

from a.binary_tree import BinaryTree


class TestBinaryTree(unittest.TestCase):
    """ 测试 binary_tree.py """

    def setUp(self) -> None:
        self.bt = BinaryTree()

    def testBinaryTree(self):
        tree = self.bt.getTree()
        self.assertEqual([0, [], []], tree)
        self.assertEqual(0, self.bt.getRootValue(tree))
        self.assertEqual([], self.bt.getLeftChild(tree))
        self.assertEqual([], self.bt.getRightChild(tree))

    def testBinaryTreeInsertLeftAndRight(self):
        tree = self.bt.getTree()
        self.assertEqual([0, [4, [], []], []], self.bt.insertLeft(tree, 4))
        self.assertEqual([0, [5, [4, [], []], []], []], self.bt.insertLeft(tree, 5))

        self.assertEqual([0, [5, [4, [], []], []], [6, [], []]], self.bt.insertRight(tree, 6))
        self.assertEqual([0, [5, [4, [], []], []], [7, [], [6, [], []]]], self.bt.insertRight(tree, 7))

        self.assertEqual(0, self.bt.getRootValue(tree))
        self.assertEqual([5, [4, [], []], []], self.bt.getLeftChild(tree))
        self.assertEqual([7, [], [6, [], []]], self.bt.getRightChild(tree))

        left = self.bt.getLeftChild(tree)
        self.assertEqual([5, [4, [], []], []], left)
        self.bt.setRootValue(left, 9)
        self.assertEqual([9, [4, [], []], []], left)
        self.assertEqual([0, [9, [4, [], []], []], [7, [], [6, [], []]]], tree)
        self.bt.insertLeft(left, 11)
        self.assertEqual([9, [11, [4, [], []], []], []], left)

        self.assertEqual([0, [9, [11, [4, [], []], []], []], [7, [], [6, [], []]]], tree)
        self.assertEqual([6, [], []], self.bt.getRightChild(self.bt.getRightChild(tree)))


if __name__ == '__main__':
    unittest.main()
