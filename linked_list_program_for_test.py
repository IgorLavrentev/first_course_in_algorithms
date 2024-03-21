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
        s_list.delete(11)
        self.assertEqual(s_list.head.value, 12)

    def test2(self): # проверка среднего элемента связанного списка
        s_list = LinkedList()
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(13))
        s_list.delete(12)
        self.assertEqual(s_list.head.next.value, 13)

    def test3(self): # проверка последнего элемента связанного списка
        s_list = LinkedList()
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(13))
        s_list.delete(13)
        self.assertEqual(s_list.tail.value, 12)

    def test4(self): 
        s_list = LinkedList()
        s_list.add_in_tail(Node(0)) # head
        s_list.add_in_tail(Node(0)) # head.next
        s_list.add_in_tail(Node(1)) # head.next.next
        s_list.add_in_tail(Node(1)) # head.next.next.next
        s_list.add_in_tail(Node(1)) # head.next.next.next.next
        s_list.add_in_tail(Node(2))
        s_list.add_in_tail(Node(2))
        s_list.delete(1)
        self.assertEqual(s_list.head.next.value, 0)
        self.assertEqual(s_list.head.next.next.value, 1)
        self.assertEqual(s_list.head.next.next.next.value, 1)
        self.assertEqual(s_list.head.next.next.next.next.value, 2)

if __name__ == '__main__':
    unittest.main()