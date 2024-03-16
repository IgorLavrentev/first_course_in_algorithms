class Node:

    def __init__(self, v):
        self.value = v # значение
        self.next = None # ссылка

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        final_list = []
        node = self.head
        while node is not None:
            if node.value == val:
                final_list.append(node)
            node = node.next
        return final_list

    def delete(self, val, all): # метод удаления всех узлов по конкретному значению
        # проверка первого элемента списка
        if self.head.value == val: 
            node_previous = self.head
            self.head = self.head.next
            if all == False:
                return
        i = 0
        # проверка середины связанного списка и его крайнего правого элемента
        node = self.head
        while node is not None: # пока указатель node не равен None

            # проверка последнего элемента списка
            if self.tail.value == val and i == s_list.len():
                node_previous.next = None
                break
            # проверка середины списка
            if node.value == val:
                node_previous.next = node.next
                if all == False:
                    break
                i += 1
                node = node.next
                continue
            i += 1
            node_previous = node
            node = node.next

    def clean(self): # очистка всего содержимого (создание пустого списка) 
        self.head.next = None
        self.head.value = None

    def len(self): # метод вычисления текущей длины списка
        LinkedList_len = 0 # переменная для подсчета длины списка
        node = self.head # начальное значение для "прохода" по всему связанному списку
        while node is not None: 
            LinkedList_len += 1
            node = node.next # переход к следующему элементу node
        return LinkedList_len

    def insert(self, afterNode, newNode): # метод вставки узла newNode
        # если переменная после которой необходимо вставить значение = None, 
        # задаем элемент как начало связанного списка "head"
        if afterNode == None: 
            newNode.next = self.head
            self.head = newNode
            return

        # поиск элемента, после которого необходимо вставить значение
        node = self.head 
        while node is not None:
            if node.value == afterNode.value:
                newNode.next = node.next
                node.next = newNode
                return
            node = node.next # переход к следующему элементу node

