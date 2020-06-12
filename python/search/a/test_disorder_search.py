import unittest

from a.disorder_search import search


class TestDisorderSearch(unittest.TestCase):

    def testDisorderSearch(self):
        items = [1, 3, 5, 7, 9]
        self.assertFalse(search(items, 0))
        self.assertTrue(search(items, 3))
        self.assertFalse(search(items, 4))
        self.assertTrue(search(items, 9))

        items = ['a', 'b', 'c', 'd']
        self.assertFalse(search(items, '$'))
        self.assertTrue(search(items, 'a'))
        self.assertFalse(search(items, '%'))
        self.assertTrue(search(items, 'd'))


if __name__ == '__main__':
    unittest.main()
