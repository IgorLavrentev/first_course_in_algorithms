class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) == 0:
            return None # если стек пустой
        el = self.stack[0]
        del self.stack[0]
        return el

    def push(self, value):
        self.stack = [value] + self.stack

    def peek(self):
        if len(self.stack) == 0:
            return None # если стек пустой
        return self.stack[0]

def parentheses(string): # функция проверки сбалансированы ли скобки
    st_1 = Stack() # стек левой скобки
    st_2 = Stack() # стек правой скобки
    i = 0 # счетчик для прохода по строке
    while i < len(string):
        if string[i] == '(':
            st_1.push('(')
        if string[i] == ')':
            st_2.push(')')
        if st_2.size() > st_1.size():
            return False
        if st_1.size() + st_2.size() == len(string) and st_1.size() == st_2.size():
            return True
        if st_1.size() + st_2.size() == len(string) and st_1.size() != st_2.size():
            return False
        i += 1
