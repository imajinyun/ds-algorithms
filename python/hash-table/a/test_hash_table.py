import unittest

from a.hash_table import HashTable


class TestHashTable(unittest.TestCase):

    def setUp(self) -> None:
        self.ht = HashTable(11)
        self.ht[54] = 'cat'
        self.ht[26] = 'dog'
        self.ht[93] = 'lion'
        self.ht[17] = 'tiger'
        self.ht[77] = 'bird'
        self.ht[31] = 'cow'
        self.ht[44] = 'goat'

    def testHashTableSize(self):
        self.assertEqual(11, self.ht.size)

    def testHashTableSlots(self):
        self.assertEqual([77, 44, None, None, 26, 93, 17, None, None, 31, 54], self.ht.slots)

    def testHashTableItems(self):
        self.assertEqual(['bird', 'goat', None, None, 'dog', 'lion', 'tiger', None, None, 'cow', 'cat'], self.ht.items)

    def testHashTableGetAndSet(self):
        self.assertEqual('bird', self.ht.get(77))

        self.ht[55] = 'pig'
        self.assertEqual('pig', self.ht.get(55))

        self.ht[20] = 'chicken'
        self.assertEqual('chicken', self.ht.get(20))
        self.assertEqual([77, 44, 55, 20, 26, 93, 17, None, None, 31, 54], self.ht.slots)

        self.ht[20] = 'duck'
        self.assertEqual('duck', self.ht.get(20))
        self.assertEqual([77, 44, 55, 20, 26, 93, 17, None, None, 31, 54], self.ht.slots)

        self.assertEqual(None, self.ht.get(99))


if __name__ == '__main__':
    unittest.main()
