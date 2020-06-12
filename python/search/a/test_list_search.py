import unittest

from a.list_search import ListSearch


class TestDisorderSearch(unittest.TestCase):
    """ 测试 list-search.py """

    def testDisorderSearch(self):
        items = [1, 3, 5, 7, 9]
        self.assertFalse(ListSearch.disorderSearch(items, 0))
        self.assertTrue(ListSearch.disorderSearch(items, 3))
        self.assertFalse(ListSearch.disorderSearch(items, 4))
        self.assertTrue(ListSearch.disorderSearch(items, 9))

        items = ['a', 'b', 'c', 'd']
        self.assertFalse(ListSearch.disorderSearch(items, '$'))
        self.assertTrue(ListSearch.disorderSearch(items, 'a'))
        self.assertFalse(ListSearch.disorderSearch(items, '%'))
        self.assertTrue(ListSearch.disorderSearch(items, 'd'))

    def testOrderSearch(self):
        items = [1, 3, 5, 7, 9]
        self.assertFalse(ListSearch.orderSearch(items, 0))
        self.assertTrue(ListSearch.orderSearch(items, 3))
        self.assertFalse(ListSearch.orderSearch(items, 4))
        self.assertTrue(ListSearch.orderSearch(items, 9))


if __name__ == '__main__':
    unittest.main()
