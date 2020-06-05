import unittest

from g.infix_to_suffix import infix_to_suffix, suffix_expr_value


class TestInfixToSuffix(unittest.TestCase):
    """ 测试 infix_to_suffix.py """

    def testInfixToSuffix(self):
        self.assertEqual('AB+C*', infix_to_suffix('(A+B)*C'))
        self.assertEqual('AB+C*', infix_to_suffix('( ( A + B ) * C )'))
        self.assertEqual('ABC*+', infix_to_suffix('A+B*C'))
        self.assertEqual('ABC*+', infix_to_suffix('( A + ( B * C ) )'))

        self.assertEqual('ABC*+D+', infix_to_suffix('A+B*C+D'))
        self.assertEqual('ABC*+D+', infix_to_suffix('( A + ( B * C ) + D)'))

        self.assertEqual('AB+CD+*', infix_to_suffix('(A+B)*(C+D)'))
        self.assertEqual('AB+CD+*', infix_to_suffix('    ( ( A + B ) * ( C + D ) )'))

        self.assertEqual('AB*CD*+', infix_to_suffix('A*B+C*D'))
        self.assertEqual('AB*CD*+', infix_to_suffix('( ( A * B ) + ( C * D ) )    '))

        self.assertEqual('AB+C+D+', infix_to_suffix('A+B+C+D'))
        self.assertEqual('AB+C+D+', infix_to_suffix(' ( A  +  B + C + D ) '))

    def testSuffixExprValue(self):
        # 6 * 5 + 6
        self.assertEqual(36, suffix_expr_value('65*6+'))

        # (6 + 5) * 6
        self.assertEqual(66, suffix_expr_value('6 5 + 6 *'))

        # 3 * 4 + 6 * 7
        self.assertEqual(54, suffix_expr_value(' 3 4 * 6 7 * + '))

        # 7 + 8 * 5 + 6
        self.assertEqual(53, suffix_expr_value('785*+6+'))

    def testSuffixExprValueError(self):
        with self.assertRaises(ValueError):
            suffix_expr_value('65%3+1')


if __name__ == '__main__':
    unittest.main()
