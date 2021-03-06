import unittest

from f.decimal_to_any import decimal_to_any, decimal_to_str


class TestDecimalToAny(unittest.TestCase):
    """ 测试 decimal_to_any.py """

    def testDecimalToAny(self):
        self.assertEqual(0, decimal_to_any(0, 2))
        self.assertEqual(1, decimal_to_any(1, 2))
        self.assertEqual(10, decimal_to_any(2, 2))
        self.assertEqual(1000, decimal_to_any(8, 2))

        self.assertEqual(0, decimal_to_any(0, 10))
        self.assertEqual(1, decimal_to_any(1, 10))
        self.assertEqual(10, decimal_to_any(10, 10))
        self.assertEqual(1000, decimal_to_any(1000, 10))

        self.assertEqual(0, decimal_to_any(0, 8))
        self.assertEqual(1, decimal_to_any(1, 8))
        self.assertEqual(12, decimal_to_any(10, 8))
        self.assertEqual(1750, decimal_to_any(1000, 8))

        self.assertEqual(0, decimal_to_any(0, 16))
        self.assertEqual(1, decimal_to_any(1, 16))
        self.assertEqual('A', decimal_to_any(10, 16))
        self.assertEqual('F', decimal_to_any(15, 16))

    def testAnyToStr(self):
        self.assertEqual('1010', decimal_to_str(10, 2))
        self.assertEqual('100001', decimal_to_str(33, 2))

        self.assertEqual('10', decimal_to_str(8, 8))
        self.assertEqual('20', decimal_to_str(16, 8))

        self.assertEqual('10', decimal_to_str(10, 10))
        self.assertEqual('99', decimal_to_str(99, 10))

        self.assertEqual('F', decimal_to_str(15, 16))
        self.assertEqual('FF', decimal_to_str(255, 16))


if __name__ == '__main__':
    unittest.main()
