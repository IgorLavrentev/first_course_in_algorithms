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
        if self.head == None:
            return None
        final_list = []
        node = self.head
        while node is not None:
            if node.value == val:
                final_list.append(node)
            node = node.next
        return final_list

    def delete(self, val, all): # метод удаления всех узлов по конкретному значению
        # исключение при пустом списке
        if self.head == None:
            return

        # исключение при удалении одного элемента
        if self.head.value == val and self.head.next == None:
            self.head.next = None
            self.head.value = None
            return

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
            if self.tail.value == val and node.next == None:
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

    # метод формирования списка всех узлов
    def all_node(self):
        final_list = []
        node = self.head
        while node is not None:
            final_list.append(node.value)
            node = node.next
        return final_list

# Тестирование

# Создание исходного списка
s_list_1 = LinkedList()
s_list_1.add_in_tail(Node(11))
s_list_1.add_in_tail(Node(12))
s_list_1.add_in_tail(Node(13))

s_list_2 = LinkedList()
s_list_2.add_in_tail(Node(11))
s_list_2.add_in_tail(Node(12))
s_list_2.add_in_tail(Node(13))

s_list_3 = LinkedList()
s_list_3.add_in_tail(Node(11))
s_list_3.add_in_tail(Node(12))
s_list_3.add_in_tail(Node(13))

# Создание итоговых списков
s_list_11 = LinkedList()
s_list_11.add_in_tail(Node(12))
s_list_11.add_in_tail(Node(13))

s_list_22 = LinkedList()
s_list_22.add_in_tail(Node(11))
s_list_22.add_in_tail(Node(12))


s_list_33 = LinkedList()
s_list_33.add_in_tail(Node(11))
s_list_33.add_in_tail(Node(13))


# Функция сравнения списков
def linked_lists_2(one, two):
    if one.len() == two.len():
        list_1 = one.all_node()
        list_2 = two.all_node()
        for i in range(one.len()):
            print('')
            if list_1[i] != list_2[i]:
                return False
        return True

# Вызов функции delete
s_list_1.delete(11, False)
s_list_2.delete(13, False)
s_list_3.delete(12, False)

# Вызов функции сравнения
print(linked_lists_2(s_list_1, s_list_11)) # удаление первого элемента
print(linked_lists_2(s_list_2, s_list_22)) # удаление второго элемента
print(linked_lists_2(s_list_3, s_list_33)) # удаление третьего элемента