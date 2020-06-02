import unittest

from stack import Stack


class StackTestCase(unittest.TestCase):
    """测试 stack.py"""

    def setUp(self) -> None:
        self.stack = Stack()

    def testStackIsEmpty(self) -> None:
        self.assertTrue(self.stack.isEmpty())

        self.stack.push(1)
        self.assertFalse(self.stack.isEmpty())

    def testStackPush(self) -> None:
        self.stack.push(1)
        self.assertEqual([1], self.stack.items)

        self.stack.push('a')
        self.assertEqual([1, 'a'], self.stack.items)

        self.stack.push(False)
        self.assertEqual([1, 'a', False], self.stack.items)

    def testStackPop(self):
        self.stack.push(1)
        self.stack.push('a')
        self.stack.push(False)
        self.stack.push(None)

        self.stack.pop()
        self.assertEqual([1, 'a', False], self.stack.items)

        self.stack.pop()
        self.assertEqual([1, 'a'], self.stack.items)

        self.stack.pop()
        self.assertEqual([1], self.stack.items)

        self.stack.pop()
        self.assertEqual([], self.stack.items)

    def testStackPeek(self) -> None:
        self.stack.push(1)
        self.assertEqual(1, self.stack.peek())

        self.stack.push('a')
        self.assertEqual('a', self.stack.peek())

        self.stack.push(True)
        self.assertEqual(True, self.stack.peek())

        self.stack.push(None)
        self.assertEqual(None, self.stack.peek())

    def testStackSize(self) -> None:
        self.stack.push(99)
        self.assertEqual(1, self.stack.size())

        self.stack.push('A')
        self.assertEqual(2, self.stack.size())

        self.stack.push(True)
        self.assertEqual(3, self.stack.size())

        self.stack.push(None)
        self.assertEqual(4, self.stack.size())

    def tearDown(self) -> None:
        del self.stack


if __name__ == '__main__':
    unittest.main()
