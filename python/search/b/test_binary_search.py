import unittest

from b.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    def testBinarySearch(self):
        items = [1, 3, 5, 7, 9]

        self.assertFalse(binary_search(items, 0))
        self.assertFalse(binary_search(items, 8))
        self.assertTrue(binary_search(items, 9))


if __name__ == '__main__':
    unittest.main()
