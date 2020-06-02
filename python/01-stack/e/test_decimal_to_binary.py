import unittest

from decimal_to_binary import decimal_to_binary


class TestDecimalToBinary(unittest.TestCase):

    def testDecimalToBinary(self):
        self.assertEqual(0, decimal_to_binary(0))
        self.assertEqual(1, decimal_to_binary(1))
        self.assertEqual(10, decimal_to_binary(2))
        self.assertEqual(100, decimal_to_binary(4))
        self.assertEqual(1000, decimal_to_binary(8))
        self.assertEqual(10000, decimal_to_binary(16))
        self.assertEqual(100000, decimal_to_binary(32))
        self.assertEqual(1000000, decimal_to_binary(64))
        self.assertEqual(10000000, decimal_to_binary(128))


if __name__ == '__main__':
    unittest.main()
