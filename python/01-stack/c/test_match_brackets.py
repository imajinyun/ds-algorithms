import unittest

from c.match_brackets import is_match_brackets


class TestMatchBrackets(unittest.TestCase):
    """ 测试 match_brackets.py """

    def testMatchBrackets(self):
        self.assertTrue(is_match_brackets('()'))
        self.assertTrue(is_match_brackets('((()))'))
        self.assertFalse(is_match_brackets('{}'))
        self.assertFalse(is_match_brackets('('))
        self.assertFalse(is_match_brackets('['))


if __name__ == '__main__':
    unittest.main()
