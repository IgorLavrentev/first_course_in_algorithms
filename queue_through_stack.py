class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) == 0:
            return None  # если стек пустой
        el = self.stack[0]
        del self.stack[0]
        return el

    def push(self, value):
        self.stack = [value] + self.stack

    def peek(self):
        if len(self.stack) == 0:
            return None  # если стек пустой
        return self.stack[0]

class Queue:
    def __init__(self):
        self.st_1 = Stack()
        self.st_2 = Stack()

    def enqueue(self, item): # вставка в хвост
        self.st_1.push(item)

    def dequeue(self): # выдача из головы
        if self.st_1.size == 0:
            return None # если очередь пустая
        for _ in range(self.st_1.size() - 1):
            self.st_2.push(self.st_1.pop())
        el = self.st_1.pop()
        for _ in range(self.st_2.size()):
            self.st_1.push(self.st_2.pop())
        return el

    def size(self):
        return self.st_1.size() # размер очереди
