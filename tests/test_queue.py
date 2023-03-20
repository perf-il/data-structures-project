"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):

    def test_str_empty(self):
        self.assertEqual(str(Queue()), '')

    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')

    def test_enqueue(self):
        self.assertEqual(self.queue.head.data, 'data1')
        self.assertEqual(self.queue.head.next_node.data, 'data2')
        self.assertEqual(self.queue.tail.data, 'data3')
        self.assertIs(self.queue.tail.next_node, None)

        with self.assertRaises(AttributeError):
            self.queue.tail.next_node.data

    def test_str(self):
        self.assertEqual(str(self.queue), "data1\ndata2\ndata3")


if __name__ == '__main__':
    unittest.main()
