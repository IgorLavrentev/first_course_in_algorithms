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

    def all_node(
        self,
    ):  # метод формирования списка значений всех элементов связанного списка
        final_list = []
        node = self.head
        while node is not None:
            final_list.append(node.value)
            node = node.next
        return final_list

# функция формирования списка каждый элемент которого
# равен сумме соответствующих элементов входных списков
def linked_lists_2(one, two):
    if one.len() == two.len():
        list_1 = one.all_node()
        list_2 = two.all_node()
        list_3 = LinkedList()
        for i in range(one.len()):
            it = list_1[i] + list_2[i]
            list_3.add_in_tail(Node(it))
        return list_3
    return None
