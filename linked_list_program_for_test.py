## Этот файл предназначен для тестирования linked_list_program.py
import unittest

from linked_list_program import Node
from linked_list_program import LinkedList

class MyTests(unittest.TestCase):
    def test1(self): # проверка удаления первого элемента связанного списка
        s_list = LinkedList()
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(13))
        s_list.delete(11)
        self.assertEqual(s_list.head.value, 12)

    def test2(self): # проверка удаления среднего элемента связанного списка
        s_list = LinkedList()
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(13))
        s_list.delete(12)
        self.assertEqual(s_list.head.next.value, 13)

    def test3(self): # проверка удаления последнего элемента связанного списка
        s_list = LinkedList()
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(13))
        s_list.delete(13)
        self.assertEqual(s_list.tail.value, 12)

    def test4(self): # проверка удаления элемента связанного списка
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

    def test5(self): # проверка связанного списка в котором один элемент
        s_list = LinkedList()
        s_list.add_in_tail(Node(11))
        s_list.delete(11)
        self.assertEqual(s_list.head, None)

    def test6(self): # проверка удаления нескольких элементов связанного списка
        s_list = LinkedList()
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(12))
        s_list.delete(11, True)
        self.assertEqual(s_list.head.value, 12)

    def test7(self): # проверка удаления нескольких элементов связанного списка
        s_list = LinkedList()
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(11))
        s_list.delete(11, True)
        self.assertEqual(s_list.head.value, 12)
        self.assertEqual(s_list.head.next.value, 12)

    def test8(self): # проверка вычисления длины связанного списка
        s_list = LinkedList()
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(12))
        self.assertEqual(s_list.len(), 4)

    def test9(self): # проверка вставки элемента в связанный список
        s_list = LinkedList()
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(13))
        s_list.insert(None, Node(10))
        self.assertEqual(s_list.head.value, 10)

    def test10(self): # проверка вставки элемента в связанный список
        s_list = LinkedList()
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(13))
        s_list.add_in_tail(Node(14))
        s_list.insert(Node(11), Node(12))
        self.assertEqual(s_list.head.next.value, 12)

    def test11(self): # проверка вставки элемента в связанный список
        s_list = LinkedList()
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(13))
        s_list.insert(Node(13), Node(14))
        self.assertEqual(s_list.tail.value, 14)

    def test12(self): # проверка вставки элемента в связанный список
        s_list = LinkedList()
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(12))
        s_list.add_in_tail(Node(14))
        s_list.insert(Node(12), Node(13))
        self.assertEqual(s_list.head.next.next.value, 13)

if __name__ == '__main__':
    unittest.main()