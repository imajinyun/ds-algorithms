import unittest

from c.binary_parse_tree import *


class TestBinaryParseTree(unittest.TestCase):

    def testBuildParseTree(self):
        tree = build_parse_tree('(3+(4*5))')
        self.assertIsInstance(tree, BinaryTree)
        self.assertEqual('+', tree.getRootValue())
        self.assertEqual(23, evaluate(tree))

        tree = build_parse_tree('( 3 + ( 4 * 5 ) )')
        self.assertEqual(23, evaluate(tree))

        self.assertEqual(1.0, evaluate(build_parse_tree('(0+(2/2))')))
        self.assertEqual(0.5, evaluate(build_parse_tree('((0+(3/2))-1)')))
        self.assertEqual(15.0, evaluate(build_parse_tree('(((0+(3/2))+1)*6)')))

    def testPreInPostOrderExpr(self):
        tree = build_parse_tree('(3+(4*5)')
        self.assertEqual('+3*45', pre_order_expr(tree))
        self.assertEqual('(3+(4*5))', in_order_expr(tree))
        self.assertEqual('(3(45*)+)', post_order_expr(tree))


if __name__ == '__main__':
    unittest.main()
