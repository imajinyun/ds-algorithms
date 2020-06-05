import unittest

from a.ordered import Ordered


class TestOrdered(unittest.TestCase):
    """ 测试 ordered.py """

    def setUp(self) -> None:
        self.ordered = Ordered()

    def testOrderedIsEmpty(self):
        self.assertTrue(self.ordered.isEmpty())

    def testOrderedAdd(self):
        self.assertEqual('', self.ordered.__str__())

        self.ordered.add(1)
        self.assertEqual('1', self.ordered.__str__())

        self.ordered.add(5)
        self.assertEqual('1->5', self.ordered.__str__())

        self.ordered.add(3)
        self.assertEqual('1->3->5', self.ordered.__str__())

        self.ordered.add(9)
        self.assertEqual('1->3->5->9', self.ordered.__str__())

        self.ordered.add(7)
        self.assertEqual('1->3->5->7->9', self.ordered.__str__())

    def testOrderedRemove(self):
        self.ordered.add('B')
        self.ordered.add('E')
        self.ordered.add('D')
        self.ordered.add('C')
        self.ordered.add('A')

        self.ordered.remove('D')
        self.assertEqual('A->B->C->E', self.ordered.__str__())

        self.ordered.remove('A')
        self.assertEqual('B->C->E', self.ordered.__str__())

        self.ordered.remove('C')
        self.assertEqual('B->E', self.ordered.__str__())

        self.ordered.remove('B')
        self.assertEqual('E', self.ordered.__str__())

        self.ordered.remove('E')
        self.assertEqual('', self.ordered.__str__())

    def testOrderedSearch(self):
        self.assertFalse(self.ordered.search('Ant'))

        self.ordered.add('Xiaomi')
        self.ordered.add('Meituan')
        self.ordered.add('Didi')
        self.ordered.add('Pinduoduo')

        self.assertTrue(self.ordered.search('Xiaomi'))
        self.assertTrue(self.ordered.search('Meituan'))
        self.assertTrue(self.ordered.search('Didi'))
        self.assertTrue(self.ordered.search('Pinduoduo'))

    def testOrderedIndex(self):
        self.assertEqual(0, self.ordered.index('ABCD'))

        self.ordered.add('C')
        self.ordered.add('A')
        self.ordered.add('B')

        self.assertEqual(1, self.ordered.index('A'))
        self.assertEqual(2, self.ordered.index('B'))
        self.assertEqual(3, self.ordered.index('C'))

    def testOrderedSize(self):
        self.assertEqual(0, self.ordered.size())

        self.ordered.add(33)
        self.assertEqual(1, self.ordered.size())

        self.ordered.add(55)
        self.assertEqual(2, self.ordered.size())

        self.ordered.add(77)
        self.assertEqual(3, self.ordered.size())


if __name__ == '__main__':
    unittest.main()
