import unittest

from a.queue import Queue


class TestQueue(unittest.TestCase):

    def setUp(self) -> None:
        self.queue = Queue()

    def testQueueIsEmpty(self):
        self.assertTrue(self.queue.isEmpty())

    def testQueueEnqueue(self):
        self.queue.enqueue(100)
        self.assertEqual([100], self.queue.items)

        self.queue.enqueue('A')
        self.assertEqual(['A', 100], self.queue.items)

        self.queue.enqueue(True)
        self.assertEqual([True, 'A', 100], self.queue.items)

        self.queue.enqueue(None)
        self.assertEqual([None, True, 'A', 100], self.queue.items)

    def testQueueDequeue(self):
        self.queue.enqueue(99)
        self.queue.enqueue('B')
        self.queue.enqueue(False)
        self.queue.enqueue(None)

        self.queue.dequeue()
        self.assertEqual([None, False, 'B'], self.queue.items)

        self.queue.dequeue()
        self.assertEqual([None, False], self.queue.items)

        self.queue.dequeue()
        self.assertEqual([None], self.queue.items)

        self.queue.dequeue()
        self.assertEqual([], self.queue.items)

    def testQueueSize(self):
        self.queue.enqueue('Z')
        self.assertEqual(1, self.queue.size())

        self.queue.enqueue(110)
        self.assertEqual(2, self.queue.size())

        self.queue.enqueue(False)
        self.assertEqual(3, self.queue.size())

        self.queue.enqueue(None)
        self.assertEqual(4, self.queue.size())

    def tearDown(self) -> None:
        del self.queue


if __name__ == '__main__':
    unittest.main()
