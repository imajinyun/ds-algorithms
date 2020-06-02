import unittest

from stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = Stack()

    def testStackPush(self) -> None:
        self.stack.push('A')
        self.assertEqual(['A'], self.stack.items)

        self.stack.push(99)
        self.assertEqual([99, 'A'], self.stack.items)

        self.stack.push(None)
        self.assertEqual([None, 99, 'A'], self.stack.items)

    def testStackPop(self):
        self.stack.push('A')
        self.stack.push(None)
        self.assertEqual([None, 'A'], self.stack.items)

        self.stack.pop()
        self.assertEqual(['A'], self.stack.items)

        self.stack.pop()
        self.assertEqual([], self.stack.items)

    def testStackPeek(self):
        self.stack.push('A')
        self.assertEqual('A', self.stack.peek())

        self.stack.push(None)
        self.assertEqual(None, self.stack.peek())

        self.stack.push(True)
        self.assertEqual(True, self.stack.peek())

    def testStackSize(self):
        self.assertEqual(0, self.stack.size())

        self.stack.push('A')
        self.assertEqual(1, self.stack.size())

        self.stack.push(None)
        self.assertEqual(2, self.stack.size())


if __name__ == '__main__':
    unittest.main()
