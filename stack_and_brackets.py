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

def parentheses(string):  # функция проверки сбалансированы ли скобки
    st = Stack()
    i = 0  # счетчик для прохода по строке
    while i < len(string):
        if string[i] == "(": # если открывающая скобка добавляем
            st.push("(")
        if string[i] == ")": # если закрывающая скобка удаляем
            st.pop()
        i += 1
    if st.size() == 0:
        return True
    if st.size() != 0:
        return False
