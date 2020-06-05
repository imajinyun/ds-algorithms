import unittest

from a.deque import Deque


class TestDeque(unittest.TestCase):
    """ 测试 deque.py """

    def setUp(self) -> None:
        self.deque = Deque()

    def testDequeIsEmpty(self):
        self.assertTrue(self.deque.isEmpty())

    def testDequeAddFront(self):
        self.deque.addFront(100)
        self.assertEqual([100], self.deque.items)

        self.deque.addFront('A')
        self.assertEqual([100, 'A'], self.deque.items)

        self.deque.addFront(True)
        self.assertEqual([100, 'A', True], self.deque.items)

        self.deque.addFront(None)
        self.assertEqual([100, 'A', True, None], self.deque.items)

    def testDequeAddRear(self):
        self.deque.addRear('B')
        self.assertEqual(['B'], self.deque.items)

        self.deque.addRear(12.88)
        self.assertEqual([12.88, 'B'], self.deque.items)

        self.deque.addRear(False)
        self.assertEqual([False, 12.88, 'B'], self.deque.items)

    def testDequeRemoveFront(self):
        self.deque.addFront('World')
        self.deque.addRear('Hello')

        self.assertEqual('World', self.deque.removeFront())
        self.assertEqual(['Hello'], self.deque.items)

        self.assertEqual('Hello', self.deque.removeFront())
        self.assertEqual([], self.deque.items)

    def testDequeRemoveRear(self):
        self.deque.addRear('USA')
        self.deque.addFront('PRC')

        self.assertEqual('USA', self.deque.removeRear())
        self.assertEqual(['PRC'], self.deque.items)

        self.deque.removeRear()
        self.assertEqual([], self.deque.items)

    def testDequeSize(self):
        self.deque.addFront('99')
        self.assertEqual(1, self.deque.size())

        self.deque.addRear(88.88)
        self.assertEqual(2, self.deque.size())


if __name__ == '__main__':
    unittest.main()
