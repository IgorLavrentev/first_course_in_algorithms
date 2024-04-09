class HashTable:
    def __init__(self, sz, stp):
        self.size = sz  # размер хэш-таблицы
        self.step = stp # длина шага (количество слотов) для поиска следующего свободного слота
        self.slots = [None] * self.size

    def hash_fun(self, value): # хэш-функция
        if len(value) > self.size or len(value) < 0:
            return None
        remainder = len(value.encode()) % self.size
        return remainder

    def seek_slot(self, value):  # находит индекс пустого слота для значения, или None
        ind = self.hash_fun(value)  # получаем индекс слота с помощью хэш-функции
        # если хэш-функция вернула None
        if ind is None:
            return None
        # если слот пустой - возвращаем индекс слота
        if self.slots[ind] is None:
            return ind
        # работа с коллизиями
        st = self.step
        for _ in range(10):
            if st == 0 or st < 0:
                return None
            # часть хэш-таблицы справа от индекса
            for i in range(ind, len(self.slots), st):
                # если слот пустой возвращаем индекс i
                if self.slots[i] is None:
                    return i
            # часть хэш-таблицы слева от индекса
            for j in range((len(self.slots) - ind) % st, ind, st):
                # если слот пустой возвращаем индекс i
                if self.slots[j] is None:
                    return j
            st -= 1
        # если свободных слотов нет
        return None

    def put(self, value):
        # присваиваем переменной 'result' значение найденного индекса слота
        result = self.seek_slot(value)
        if result is None:
            return None  # если из-за коллизий элемент не удаётся разместить
        self.slots[result] = value # добавляем значение в хэш-таблицу
        return result # возвращаем индекс слота

    def find(self, value):  # находит индекс слота со значением, или None
        for i in range(len(self.slots)):
            if self.slots[i] == value:
                return i
        return None
