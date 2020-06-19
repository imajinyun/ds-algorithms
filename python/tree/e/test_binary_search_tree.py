import unittest

from e.binary_search_tree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    def testBinarySearchTreeLength(self):
        bst = BinarySearchTree()
        self.assertEqual(0, bst.length())

    def testBinarySearchTreeGetAndPut(self):
        bst = BinarySearchTree()
        bst.put(1, 'a')
        self.assertEqual('a', bst.get(1))

        bst.put(2, 'b')
        self.assertEqual('b', bst.get(2))

        bst.put(3, 'c')
        self.assertEqual('c', bst.get(3))

        bst.put(4, 'd')
        self.assertEqual('d', bst.get(4))

        bst.put(5, 'e')
        self.assertEqual('e', bst.get(5))

        bst.put(6, 'f')
        self.assertEqual('f', bst.get(6))

        keys = []
        [keys.append(node) for node in bst]
        self.assertListEqual([1, 2, 3, 4, 5, 6], keys)
        self.assertListEqual(['a', 'b', 'c', 'd', 'e', 'f'], bst.getTreeValues())

    def testBinarySearchTreeDeleteNodeWithoutChildNode(self):
        bst = BinarySearchTree()
        values = [17, 5, 35, 2, 11, 29, 38, 9, 16, 8]
        [bst.put(i, i) for i in values]
        self.assertListEqual(values, bst.getTreeValues())

        bst.delete(16)
        self.assertEqual(len(values) - 1, len(bst.getTreeValues()))
        self.assertListEqual([17, 5, 35, 2, 11, 29, 38, 9, 8], bst.getTreeValues())

    def testBinarySearchTreeDeleteNodeOnlyOneNode(self):
        bst = BinarySearchTree()
        values = [17, 5, 25, 2, 11, 35, 9, 16, 29, 38, 7]
        [bst.put(i, i) for i in values]
        self.assertEqual(values, bst.getTreeValues())

        bst.delete(25)
        self.assertEqual(len(values) - 1, len(bst.getTreeValues()))
        self.assertEqual([17, 5, 35, 2, 11, 29, 38, 9, 16, 7], bst.getTreeValues())

    def testBinarySearchTreeDeleteNodeHasTwoNode(self):
        bst = BinarySearchTree()
        values = [17, 5, 35, 2, 11, 29, 38, 9, 16, 7, 8]
        [bst.put(i, i) for i in values]
        self.assertEqual(values, bst.getTreeValues())

        bst.delete(5)
        self.assertEqual(len(values) - 1, len(bst.getTreeValues()))
        self.assertEqual([17, 7, 35, 2, 11, 29, 38, 9, 16, 8], bst.getTreeValues())

    def testBinarySearchTreeDelete(self):
        bst = BinarySearchTree()
        bst.put(1, 'A')
        bst.put(2, 'B')
        bst.put(3, 'C')
        bst.put(4, 'D')
        bst.put(5, 'E')

        bst.delete(2)
        self.assertEqual(4, bst.length())

        self.assertEqual(['A', 'C', 'D', 'E'], bst.getTreeValues())

        bst.delete(3)
        keys = []
        [keys.append(k) for k in bst]
        self.assertEqual([1, 4, 5], keys)
        self.assertEqual(['A', 'D', 'E'], bst.getTreeValues())


if __name__ == '__main__':
    unittest.main()
