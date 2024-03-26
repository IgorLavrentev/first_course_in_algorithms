class Node:

    def __init__(self, v):
        self.value = v  # значение
        self.next = None  # ссылка


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

    def len(self):
        LinkedList_len = 0
        node = self.head
        while node is not None:
            LinkedList_len += 1
            node = node.next
        return LinkedList_len

    def print_all_nodes(self):
        node = self.head
        while node is None:
            print(node.value)
            node = node.next


# функция формирования списка каждый элемент которого
# равен сумме соответствующих элементов входных списков
def linked_lists_2(one, two):
    if one.len() != two.len():
        return None
    final_list = LinkedList()  # итоговый список
    node_1 = one.head
    node_2 = two.head
    while node_1 is not None:
        it = node_1.value + node_2.value  # вычисление суммы
        final_list.add_in_tail(Node(it))  # добавление суммы
        node_1 = node_1.next
        node_2 = node_2.next
    return final_list
