## Этот файл предназначен для тестирования linked_list_program.py
import unittest

from linked_list_program import Node
from linked_list_program import LinkedList

class MyTests(unittest.TestCase):
    def test1(self): # проверка первого элемента связанного списка
        s_list = LinkedList()
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(13))
        s_list.delete(11, False)
        self.assertEqual(s_list.head.value, 12)

    def test2(self): # проверка среднего элемента связанного списка
        s_list = LinkedList()
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(13))
        s_list.delete(12, False)
        self.assertEqual(s_list.head.next.value, 13)

    def test3(self): # проверка последнего элемента связанного списка
        s_list = LinkedList()
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(13))
        s_list.delete(13, False)
        self.assertEqual(s_list.tail.value, 12)

if __name__ == '__main__':
    unittest.main()