"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_str_empty(self):
        self.assertEqual(str(LinkedList()), 'None')

    def setUp(self):
        self.ll = LinkedList()
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_at_end({'id': 3})
        self.ll.insert_beginning({'id': 0})

    def test_ll(self):
        self.assertEqual(self.ll.head.data, {'id': 0})
        self.assertEqual(self.ll.head.next_node.data, {'id': 1})
        self.assertEqual(self.ll.tail.data, {'id': 3})
        self.assertIs(self.ll.tail.next_node, None)

        with self.assertRaises(AttributeError):
            self.ll.tail.next_node.data

    def test_str(self):
        self.assertEqual(str(self.ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")

    def test_to_list(self):
        self.assertEqual(self.ll.to_list(), [{'id': 0}, {'id': 1}, {'id': 2}, {'id': 3}])

    def test_get_data_by_id(self):
        self.assertEqual(self.ll.get_data_by_id(0), {'id': 0})
        self.assertEqual(self.ll.get_data_by_id(1), {'id': 1})
        self.assertEqual(self.ll.get_data_by_id(2), {'id': 2})
        self.assertEqual(self.ll.get_data_by_id(3), {'id': 3})
        self.assertEqual(self.ll.get_data_by_id(13), None)
        self.assertEqual(self.ll.get_data_by_id('ghjgj'), None)
        self.assertEqual(self.ll.get_data_by_id([1, 2, 3]), None)


if __name__ == '__main__':
    unittest.main()
