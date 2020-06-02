import unittest

from match_brackets import is_match_brackets


class TestMatchBrackets(unittest.TestCase):

    def testMatchBrackets(self):
        self.assertTrue(is_match_brackets('()'))
        self.assertTrue(is_match_brackets('((()))'))
        self.assertFalse(is_match_brackets('{}'))
        self.assertFalse(is_match_brackets('('))
        self.assertFalse(is_match_brackets('['))


if __name__ == '__main__':
    unittest.main()
