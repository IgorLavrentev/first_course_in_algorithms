class Stack:
    def __init__(self):
        self.stack = []

    def size(self): # метод длины стека
        return len(self.stack)

    def pop(self): # метод удаления последнего добавленного элемента
        if len(self.stack) == 0:
            return None # если стек пустой
        el = self.stack[0]
        del self.stack[0]
        return el

    def push(self, value): # метод добавления элемента
        self.stack = [value] + self.stack

    def peek(self): # метод "возврата" последнего добавленного элемента
        if len(self.stack) == 0:
            return None # если стек пустой
        return self.stack[0]
