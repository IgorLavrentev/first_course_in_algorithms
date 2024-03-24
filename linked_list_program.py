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
        while node is not None:
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
        if self.head is None:
            return final_list
        node = self.head
        while node is not None:
            if node.value == val:
                final_list.append(node)
            node = node.next
        return final_list

    def delete(self, val, all = False): # метод удаления всех узлов по конкретному значению
        # исключение при пустом списке
        if self.head is None:
            return

        # исключение при удалении одного элемента
        if self.head.value == val and self.head.next is None:
            self.head = None
            self.tail = None
            return

        # проверка середины связанного списка и его крайнего правого элемента
        node = self.head
        node_previous = self.head
        while node is not None: # пока указатель node не равен None
            # проверка первого элемента списка
            if self.head.value == val:
                self.head = self.head.next
                if all is False:
                    return
                continue
            # проверка последнего элемента списка
            if self.tail.value == val and node.next is None:
                node_previous.next = None
                self.tail.value = node_previous.value
                return
            # проверка середины списка
            if node.value == val:
                node_previous.next = node.next
                if all is False:
                    return
                node = node.next
                continue
            # переход к следующему значению списка
            node_previous = node
            node = node.next
        return

    def clean(self): # очистка всего содержимого (создание пустого списка)
        self.head = None
        self.tail = None

    def len(self): # метод вычисления текущей длины списка
        LinkedList_len = 0 # переменная для подсчета длины списка
        node = self.head # начальное значение для "прохода" по всему связанному списку
        while node is not None:
            LinkedList_len += 1
            node = node.next # переход к следующему элементу node
        return LinkedList_len

    def insert(self, afterNode, newNode): # метод вставки узла newNode
        # вставка элемента в пустой список
        if afterNode is None and self.head is None:
            self.head = newNode
            self.tail = newNode
            return

        # если переменная после которой необходимо вставить значение = None,
        # задаем элемент как начало связанного списка "head"
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            return

        # поиск элемента, после которого необходимо вставить значение
        node = self.head
        while node is not None:
            if self.tail.value == afterNode.value and node.next is None:
                newNode.next = None
                node.next = newNode
                self.tail = newNode
                return
            if node.value == afterNode.value:
                newNode.next = node.next
                node.next = newNode
                return
            node = node.next # переход к следующему элементу node
