import unittest

from a.decimal_to_any import decimal_to_any as fn


class TestDecimalToAny(unittest.TestCase):
    """ 测试 decimal_to_any.py """

    def testDecimalToAny(self):
        self.assertEqual('1010', fn(10, 2))
        self.assertEqual('11111', fn(31, 2))

        self.assertEqual('12', fn(10, 8))
        self.assertEqual('15', fn(13, 8))

        self.assertEqual('10', fn(10, 10))
        self.assertEqual('88', fn(88, 10))

        self.assertEqual('A', fn(10, 16))
        self.assertEqual('10', fn(16, 16))


if __name__ == '__main__':
    unittest.main()
