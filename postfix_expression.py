class Stack:
    def __init__(self):
        self.stack = []

    def size(self):  # метод длины стека
        return len(self.stack)

    def pop(self):  # метод удаления последнего добавленного элемента
        if len(self.stack) == 0:
            return None  # если стек пустой
        el = self.stack[0]
        del self.stack[0]
        return el

    def push(self, value):  # метод добавления элемента
        self.stack = [value] + self.stack

    def peek(self):  # метод "возврата" последнего добавленного элемента
        if len(self.stack) == 0:
            return None  # если стек пустой
        return self.stack[0]

def postfix(entry_stack):  # функция для реализации постфиксной записи выражения
    second_stack = Stack()
    for _ in range(entry_stack.size()):  # "проход" по всему списку
        if entry_stack.peek().isdigit():  # если очередное значение типа int
            second_stack.push(entry_stack.pop())  # добавляем во второй список
            continue
        if entry_stack.peek() == "=": # возврат результата функции
            return second_stack.peek()
        x = int(second_stack.pop())
        y = int(second_stack.pop())
        if entry_stack.peek() == "+": # сложение
            second_stack.push(x + y)
        if entry_stack.peek() == "*": # умножение
            second_stack.push(x * y)
        if entry_stack.peek() == "-": # вычитание
            second_stack.push(y - x)
        if entry_stack.peek() == "/": # деления
            second_stack.push(y / x)
        entry_stack.pop()
