class Deque:
    def __init__(self):
        self.deque = []  # инициализация хранилища данных

    def addFront(self, item):  # добавление в голову
        self.deque = [item] + self.deque

    def addTail(self, item):  # добавление в хвост
        self.deque.append(item)

    def removeFront(self):  # удаление из головы
        if len(self.deque) == 0:
            return None  # если очередь пустая
        el = self.deque[0]
        self.deque = self.deque[1 : len(self.deque)]
        return el

    def removeTail(self):  # удаление из хвоста
        if len(self.deque) == 0:
            return None  # если очередь пустая
        el = self.deque[len(self.deque) - 1]
        self.deque = self.deque[: len(self.deque) - 1]
        return el

    def size(self):
        return len(self.deque)  # размер очереди


def palindrome(string):
    de = Deque()
    string = string.replace(" ", "")
    for i in range(len(string)):
        de.addFront(string[i])
    for _ in range(int(len(string) / 2)):
        if de.removeFront() == de.removeTail():
            continue
        return False
    return True
