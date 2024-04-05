class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        if v1 == v2:
            return 0
        if v1 > v2:
            return 1
        return None

    def add(self, value):
        # создание узла
        insert_node = Node(value)
        # вставка в пустой список
        if self.head is None:
            self.head = insert_node
            self.tail = insert_node
            return
        # вставка в начало (ascending = True or False)
        if (
            self.compare(value, self.head.value) == -1 and self.__ascending is True
        ) or (self.compare(value, self.head.value) == 1 and self.__ascending is False):
            self.head.prev = insert_node
            insert_node.next = self.head
            self.head = insert_node
            return

        node = self.head
        while node is not None:
            # вставка в конец (ascending = True or False)
            if node.next is None and (
                self.compare(value, node.value) == 0
                or (
                    (
                        self.compare(value, self.tail.value) == 1
                        and self.__ascending is True
                    )
                    or (
                        self.compare(value, self.tail.value) == -1
                        and self.__ascending is False
                    )
                )
            ):
                self.tail.next = insert_node
                insert_node.prev = self.tail
                self.tail = insert_node
                return

            # вставка в середину (ascending = True or False)
            if (
                (
                    self.compare(value, node.value) == 1
                    or self.compare(value, node.value) == 0
                )
                and (self.compare(value, node.next.value) == -1)
                and self.__ascending is True
            ) or (
                (
                    self.compare(value, node.value) == -1
                    or self.compare(value, node.value) == 0
                )
                and (self.compare(value, node.next.value) == 1)
                and self.__ascending is False
            ):
                # следующий элемент
                node.next.prev = insert_node
                # элемент для вставки
                insert_node.prev = node
                insert_node.next = node.next
                # текущий элемент
                node.next = insert_node.value
                node.next = insert_node
                return
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            # прерывание поиска
            if self.__ascending is True and node.value > val:
                return None
            if self.__ascending is False and node.value < val:
                return None
            node = node.next
        return None

    def delete(self, val):
        # исключение при пустом списке
        if self.head is None:
            return
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
                return
            # проверка середины списка
            if node.value == val:
                node.next.prev = node.prev
                node.prev.next = node.next
                return
            # переход к следующему значению списка
            node = node.next
        return

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        LinkedList_len = 0  # переменная для подсчета длины списка
        node = self.head  # начальное значение для "прохода" по всему связанному списку
        while node is not None:
            LinkedList_len += 1
            node = node.next  # переход к следующему элементу node
        return LinkedList_len

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):  # переопределённая версия для строк
        if v1.strip() < v2.strip():
            return -1
        if v1.strip() == v2.strip():
            return 0
        if v1.strip() > v2.strip():
            return 1
        return None
