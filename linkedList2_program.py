class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

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

    def delete(self, val, all=False):
        # исключение при пустом списке
        if self.head is None:
            return
        # проверка середины связанного списка и его крайнего правого элемента
        node = self.head
        while node is not None:  # пока указатель node не равен None
            # исключение при удалении одного элемента
            if self.head.value == val and self.head.next is None:
                self.head = None
                self.tail = None
                return
            # проверка последнего элемента списка
            if self.tail.value == val and node.next is None:
                self.tail = self.tail.prev
                self.tail.next = None
                return
            # проверка первого элемента списка
            if self.head.value == val:
                self.head = self.head.next
                self.head.prev = None
                if all is False:
                    return
                node = node.next
                continue
            # проверка середины списка
            if node.value == val:
                node.next.prev = node.prev
                node.prev.next = node.next
                if all is False:
                    return
                node = node.next
                continue
            # переход к следующему значению списка
            node = node.next
        return

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        LinkedList_len = 0  # переменная для подсчета длины списка
        node = self.head  # начальное значение для "прохода" по всему связанному списку
        while node is not None:
            LinkedList_len += 1
            node = node.next  # переход к следующему элементу node
        return LinkedList_len

    def insert(self, afterNode, newNode):
        # вставка элемента в пустой список
        if afterNode is None and self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        # если переменная после которой необходимо вставить значение = None,
        # помещаем новый элемент в конец списка
        if afterNode is None:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            return
        # поиск элемента, после которого необходимо вставить значение
        node = self.head
        while node is not None:
            if self.tail.value == afterNode.value and node.next is None:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
                return
            if node.value == afterNode.value:
                # следующий элемент
                node.next.prev = newNode
                # элемент для вставки
                newNode.prev = node
                newNode.next = node.next
                # текущий элемент
                node.next = newNode.value
                node.next = newNode
                return
            node = node.next  # переход к следующему элементу node

    def add_in_head(self, newNode):
        # вставка элемента в пустой список
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        # вставка элемента в не пустой список
        newNode.next = self.head
        self.head = newNode
        return
