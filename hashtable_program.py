class HashTable:
    def __init__(self, sz, stp):
        self.size = sz  # размер хэш-таблицы
        self.step = stp # длина шага (количество слотов) для поиска следующего свободного слота
        self.slots = [None] * self.size

    def hash_fun(self, value): # хэш-функция
        if len(value) >= self.size or len(value) < 0:
            return None
        remainder = len(value.encode()) % self.size
        return remainder

    def seek_slot(self, value):  # находит индекс пустого слота для значения, или None
        ind = self.hash_fun(value)  # получаем индекс слота
        # если хэш-функция вернула None
        if ind is None:
            return None
        # если слот пустой - возвращаем индекс слота
        if self.slots[ind] is None:
            return ind
        # работа с коллизиями
        st = self.step
        for _ in range(2):
            i = ind + st
            while i != ind:
                # переход в начало списка с учетом шага
                if i >= len(self.slots):
                    i = i - len(self.slots)
                # если слот пустой возвращаем индекс i
                if self.slots[i] is None:
                    return i
                # переход к следующему значению
                i += st
            st += 1
        return None

    def put(self, value):
        # присваиваем переменной 'result' значение по хэш-функции
        result = self.seek_slot(value)
        if result is None:
            return None  # если из-за коллизий элемент не удаётся разместить
        self.slots[result] = value
        return result

    def find(self, value):  # находит индекс слота со значением, или None
        for i in range(len(self.slots)):
            if self.slots[i] == value:
                return self.hash_fun(value)
        return None
