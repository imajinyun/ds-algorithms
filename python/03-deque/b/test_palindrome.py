import unittest

from b.palindrome import palindrome


class TestPalindrome(unittest.TestCase):

    def testPalindrome(self):
        self.assertFalse(palindrome('python'))
        self.assertTrue(palindrome('madam'))
        self.assertFalse(palindrome('1234567890'))
        self.assertFalse(palindrome(str(1234567890)))
        self.assertTrue(palindrome('12321'))
        self.assertTrue(palindrome('abcdeedcba'))
        self.assertTrue(palindrome(str(12321)))
        self.assertTrue(palindrome(str(124421)))


if __name__ == '__main__':
    unittest.main()
