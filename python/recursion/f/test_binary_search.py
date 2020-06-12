import unittest

from f.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    def testBinarySearch(self):
        items = [2, 4, 6, 8]
        self.assertFalse(binary_search(items, 0))
        self.assertTrue(binary_search(items, 2))
        self.assertFalse(binary_search(items, 5))
        self.assertTrue(binary_search(items, 8))


if __name__ == '__main__':
    unittest.main()
