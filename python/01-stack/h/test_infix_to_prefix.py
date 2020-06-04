import unittest

from h.infix_to_prefix import infix_to_prefix, prefix_expr_value


class TestInfixToPrefix(unittest.TestCase):
    """ 测试 infix_to_prefix.py """

    def testInfixToPrefix(self):
        self.assertEqual('+AB', infix_to_prefix('A+B'))
        self.assertEqual('+AB', infix_to_prefix('(A+B)'))
        self.assertEqual('+AB', infix_to_prefix(' ( A + B ) '))

        self.assertEqual('+A*BC', infix_to_prefix('A+B*C'))
        self.assertEqual('+A*BC', infix_to_prefix('(A+(B*C))'))
        self.assertEqual('+A*BC', infix_to_prefix(' ( A + ( B * C ) ) '))

        self.assertEqual('*+ABC', infix_to_prefix('(A+B)*C'))
        self.assertEqual('*+ABC', infix_to_prefix('((A+B)*C)'))
        self.assertEqual('*+ABC', infix_to_prefix(' ( ( A + B ) * C ) '))

        self.assertEqual('++A*BCD', infix_to_prefix('A+B*C+D'))
        self.assertEqual('++A*BCD', infix_to_prefix('((A+(B*C))+D)'))
        self.assertEqual('++A*BCD', infix_to_prefix(' ( ( A + ( B * C ) ) + D ) '))

        self.assertEqual('+*AB*CD', infix_to_prefix('A*B+C*D'))
        self.assertEqual('+*AB*CD', infix_to_prefix('((A*B)+(C*D))'))
        self.assertEqual('+*AB*CD', infix_to_prefix(' ( ( A * B ) + ( C * D ) ) '))

        self.assertEqual('*+AB+CD', infix_to_prefix('(A+B)*(C+D)'))
        self.assertEqual('*+AB+CD', infix_to_prefix('((A+B)*(C+D))'))
        self.assertEqual('*+AB+CD', infix_to_prefix(' ( A + B ) * ( C + D ) '))

        self.assertEqual('+++ABCD', infix_to_prefix('A+B+C+D'))
        self.assertEqual('+++ABCD', infix_to_prefix('(((A+B)+C)+D)'))
        self.assertEqual('+++ABCD', infix_to_prefix(' ( ( ( A + B ) + C ) + D ) '))

    def testPrefixExprValue(self):
        # 6 * 5 + 6
        self.assertEqual(36, prefix_expr_value('+*656'))

        # (6 + 5) * 6
        self.assertEqual(66, prefix_expr_value('* + 6 5 6'))

        # 3 * 4 + 6 * 7
        self.assertEqual(54, prefix_expr_value(' + * 3 4 * 6 7'))

        # 7 + 8 * 5 + 6
        self.assertEqual(53, prefix_expr_value('++7*856'))

    def testPrefixExprValueError(self):
        with self.assertRaises(ValueError):
            prefix_expr_value('+%653')


if __name__ == '__main__':
    unittest.main()
