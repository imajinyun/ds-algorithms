import unittest

from d.binary_tree import BinaryTree


class TestOrderTraversal(unittest.TestCase):
    """ 测试 *order_traversal.py """

    def setUp(self) -> None:
        self.items = []
        self.tree = BinaryTree('A')
        self.tree.insertLeft('B')
        self.tree.insertRight('G')
        self.tree.getLeftChild().insertLeft('C')
        self.tree.getLeftChild().insertRight('D')
        self.tree.getLeftChild().getRightChild().insertLeft('E')
        self.tree.getLeftChild().getRightChild().insertRight('F')
        self.tree.getRightChild().insertLeft('H')
        self.tree.getRightChild().insertRight('I')

    def testBinaryTreeInsertNode(self):
        self.assertEqual('A', self.tree.getRootValue())

        self.tree.insertLeft('B')
        self.assertEqual('B', self.tree.getLeftChild().getRootValue())

        self.tree.insertRight('G')
        self.assertEqual('G', self.tree.getRightChild().getRootValue())

        self.tree.getLeftChild().insertLeft('C')
        self.assertEqual('C', self.tree.getLeftChild().getLeftChild().getRootValue())

        self.tree.getLeftChild().insertRight('D')
        self.assertEqual('D', self.tree.getLeftChild().getRightChild().getRootValue())

        self.tree.getLeftChild().getRightChild().insertLeft('E')
        self.assertEqual('E', self.tree.getLeftChild().getRightChild().getLeftChild().getRootValue())

        self.tree.getLeftChild().getRightChild().insertRight('F')
        self.assertEqual('F', self.tree.getLeftChild().getRightChild().getRightChild().getRootValue())

        self.tree.getRightChild().insertLeft('H')
        self.assertEqual('H', self.tree.getRightChild().getLeftChild().getRootValue())

        self.tree.getRightChild().insertRight('I')
        self.assertEqual('I', self.tree.getRightChild().getRightChild().getRootValue())

    def testPreOrderTraversal(self):
        """
        按根左右次序遍历：
           A
         B   G
        C D H I
         E F
        """
        self.tree.preOrder(self.items)
        self.assertEqual(['A', 'B', 'G', 'C', 'D', 'H', 'I', 'E', 'F'], self.tree.getTreeValues(self.tree))
        self.assertEqual(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], self.items)

    def testInOrderTraversal(self):
        """
        按左根右次序遍历：
           A
         B   G
        C D H I
         E F
        """
        self.tree.inOrder(self.items)
        self.assertEqual(['A', 'B', 'G', 'C', 'D', 'H', 'I', 'E', 'F'], self.tree.getTreeValues(self.tree))
        self.assertEqual(['C', 'B', 'E', 'D', 'F', 'A', 'H', 'G', 'I'], self.items)

    def testPostOrderTraversal(self):
        """
        按左右根次序遍历：
           A
         B   G
        C D H I
         E F
        """
        self.tree.postOrder(self.items)
        self.assertEqual(['A', 'B', 'G', 'C', 'D', 'H', 'I', 'E', 'F'], self.tree.getTreeValues(self.tree))
        self.assertEqual(['C', 'E', 'F', 'D', 'B', 'H', 'I', 'G', 'A'], self.items)


if __name__ == '__main__':
    unittest.main()
