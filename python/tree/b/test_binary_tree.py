import unittest

from b.binary_tree import BinaryTree


class TestBinaryTree(unittest.TestCase):

    def setUp(self) -> None:
        self.bt = BinaryTree('a')

    def testRootValue(self):
        self.assertEqual('a', self.bt.getRootValue())

    def testGetLeftChild(self):
        self.assertEqual(None, self.bt.getLeftChild())

    def testGetRightChild(self):
        self.assertEqual(None, self.bt.getRightChild())

    def testBinaryTreeInsertLeftAndRight(self):
        self.bt.insertLeft('b')
        self.assertEqual('b', self.bt.getLeftChild().getRootValue())

        self.bt.insertRight('c')
        self.assertEqual('c', self.bt.getRightChild().getRootValue())

        self.bt.setRootValue('Hello World')
        self.assertEqual('Hello World', self.bt.getRootValue())

        self.bt.getRightChild().setRootValue('PRC')
        self.assertEqual('PRC', self.bt.getRightChild().getRootValue())

        self.bt.getLeftChild().insertLeft('d')
        self.assertEqual('d', self.bt.getLeftChild().getLeftChild().getRootValue())


if __name__ == '__main__':
    unittest.main()
