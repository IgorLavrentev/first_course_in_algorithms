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
        if ind is None:
            return None
        # работа с коллизиями
        if self.slots[ind] is None:
            return ind
        for _ in range(2):
            for i in range(ind, len(self.slots), self.step):
                if self.slots[i] is None:
                    return i
            self.step = self.step + 1
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
