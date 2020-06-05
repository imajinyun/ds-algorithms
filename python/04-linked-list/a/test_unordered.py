import unittest

from a.unordered import Unordered


class TestUnordered(unittest.TestCase):

    def setUp(self) -> None:
        self.unordered = Unordered()

    def testUnorderedIsEmpty(self):
        self.assertTrue(self.unordered.isEmpty())

    def testUnorderedAdd(self):
        self.unordered.add(8)
        self.assertEqual('8', self.unordered.__str__())

        self.unordered.add('a')
        self.assertEqual('a->8', self.unordered.__str__())

        self.unordered.add(True)
        self.assertEqual('True->a->8', self.unordered.__str__())

    def testUnorderedRemove(self):
        self.unordered.add('a')
        self.unordered.add('b')
        self.unordered.add('c')
        self.unordered.add('d')

        self.unordered.remove('a')
        self.assertEqual('d->c->b', self.unordered.__str__())

        self.unordered.remove('b')
        self.assertEqual('d->c', self.unordered.__str__())

        self.unordered.remove('c')
        self.assertEqual('d', self.unordered.__str__())

        self.unordered.remove('d')
        self.assertEqual('', self.unordered.__str__())

        self.unordered.add(1)
        self.unordered.add(2)
        self.unordered.add(3)

        self.assertEqual('3->2->1', self.unordered.__str__())
        self.unordered.remove(1)
        self.assertEqual('3->2', self.unordered.__str__())

    def testUnorderedSearch(self):
        self.assertFalse(self.unordered.search(100))

        self.unordered.add('AA')
        self.assertTrue(self.unordered.search('AA'))

        self.unordered.add('BB')
        self.assertTrue(self.unordered.search('BB'))

        self.unordered.add(True)
        self.assertTrue(self.unordered.search(True))

        self.unordered.add(None)
        self.assertTrue(self.unordered.search(None))

        self.assertFalse(self.unordered.search(False))

    def testUnorderedIndex(self):
        self.assertEqual(0, self.unordered.index(True))

        self.unordered.add('Google')
        self.assertEqual(1, self.unordered.index('Google'))

        self.unordered.add('Alibaba')
        self.assertEqual(2, self.unordered.index('Alibaba'))

        self.unordered.add('Facebook')
        self.assertEqual(3, self.unordered.index('Facebook'))

        self.unordered.add('Tencent')
        self.assertEqual(4, self.unordered.index('Tencent'))

    def testUnorderedSize(self):
        self.assertEqual(0, self.unordered.size())

        self.unordered.add(1)
        self.assertEqual(1, self.unordered.size())

        self.unordered.add(2)
        self.assertEqual(2, self.unordered.size())

        self.unordered.remove(1)
        self.assertEqual(1, self.unordered.size())

        self.unordered.remove(2)
        self.assertEqual(0, self.unordered.size())


if __name__ == '__main__':
    unittest.main()
