class HashTable:
    def __init__(self, sz, stp):
        self.size_table = sz  # размер хэш-таблицы
        self.step = (
            stp  # длина шага (количество слотов) для поиска следующего свободного слота
        )
        self.slots = [None] * self.size_table

    def hash_fun(self, value):  # хэш-функция
        if len(value) > self.size_table or len(value) < 0:
            return None
        remainder = len(value.encode()) % self.size_table
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
        self.slots[result] = value  # добавляем значение в хэш-таблицу
        return result  # возвращаем индекс слота

    def find(self, value):  # находит индекс слота со значением, или None
        for i in range(len(self.slots)):
            if self.slots[i] == value:
                return i
        return None

# наследуемый от HashTable класс
class PowerSet(HashTable):

    def __init__(self, sz, stp):
        if sz > 0 and stp > 0:
            super(PowerSet, self).__init__(sz, stp)
        else: # исключение при вызове конструктора
            raise ValueError

    def size(self):  # количество элементов в множестве
        return len(self.slots)

    def put(self, value):
        for v in range(len(self.slots)):  # нахождение индекса ключа в массиве ключей
            if self.slots[v] == value:
                return None
        # присваиваем переменной 'result' значение найденного индекса слота
        result = self.seek_slot(value)
        if result is None:
            return None  # если из-за коллизий элемент не удаётся разместить
        self.slots[result] = value  # добавляем значение в хэш-таблицу
        return result  # возвращаем индекс слота

    def get(self, value):  # возвращает True если value имеется в множестве, иначе False
        for j in range(self.size_table):
            if self.slots[j] == value:
                return True
        return False

    def remove(self, value):  # возвращает True если value удалено, иначе False
        for j in range(self.size_table):
            if self.slots[j] == value:
                self.slots[j] = None
                return True
        return False

    def intersection(self, set2):  # пересечение текущего множества и set2
        if set2.size() == 0 or self.size_table == 0:
            return None
        counter = 0  # счетчик
        # создание максимально возможной хэш-таблицы
        if self.size_table >= set2.size():
            set3 = PowerSet(self.size_table, self.size_table // 10)
        if self.size_table < set2.size():
            set3 = PowerSet(set2.size(), set2.size() // 10)
        # сравнение хэш-таблиц
        for el_1 in range(set2.size()):
            for el_2 in range(self.size_table):
                if (
                    set2.slots[el_1] == self.slots[el_2]
                    and set2.slots[el_1] is not None
                    and self.slots[el_2] is not None
                ):
                    set3.put(set2.slots[el_1])
                    counter += 1
        # проверка на наличее минимум одного элемента пересечения
        if counter == 0:
            return None
        # создание хэш-таблицы только с элементами пересечения
        if counter // 10 < 2:
            step_intersection = 1
        if counter // 10 >= 2:
            step_intersection = counter // 10
        set4 = PowerSet(counter, step_intersection)
        for el_3 in range(set3.size()):
            if set3.slots[el_3] is not None:
                set4.put(set3.slots[el_3])
        return set4

    def union(self, set2):  # объединение текущего множества и set2
        if set2.size() == 0 or self.size_table == 0:
            return None
        counter = 0  # счетчик
        # создание максимально возможной хэш-таблицы
        if self.size_table // 10 < 2:
            step_un = 1
        if self.size_table // 10 >= 2:
            step_un = (self.size_table + set2.size()) // 10
        set3 = PowerSet(self.size_table + set2.size(), step_un)
        # сравнение хэш-таблиц
        for el_1 in range(set2.size()):
            for el_2 in range(self.size_table):
                if (
                    set2.slots[el_1] == self.slots[el_2]
                    and set2.slots[el_1] is not None
                    and self.slots[el_2] is not None
                ):
                    set3.put(set2.slots[el_1])
                    set2.slots[el_1] = None
                    self.slots[el_2] = None
                    counter += 1
                    continue
                if self.slots[el_2] is not None and set2.get(self.slots[el_2]) is False:
                    set3.put(self.slots[el_2])
                    self.slots[el_2] = None
                    counter += 1
                    continue
                if set2.slots[el_1] is not None and self.get(set2.slots[el_1]) is False:
                    set3.put(set2.slots[el_1])
                    set2.slots[el_1] = None
                    counter += 1
                    continue
        # проверка на наличее минимум одного элемента пересечения
        if counter == 0:
            return None
        # создание хэш-таблицы только со всеми элементами
        if counter // 10 < 2:
            step_union = 1
        if counter // 10 >= 2:
            step_union = counter // 10
        set4 = PowerSet(counter, step_union)
        for el_3 in range(set3.size()):
            if set3.slots[el_3] is not None:
                set4.put(set3.slots[el_3])
        return set4

    def difference(self, set2):  # разница текущего множества и set2
        counter = 0  # счетчик
        # создание максимально возможной хэш-таблицы
        if self.size_table // 10 < 2:
            step_un = 1
        if self.size_table // 10 >= 2:
            step_un = (self.size_table + set2.size()) // 10
        set3 = PowerSet(self.size_table + set2.size(), step_un)
        # сравнение хэш-таблиц
        for _ in range(set2.size()):
            for el_2 in range(self.size_table):
                if self.slots[el_2] is not None and set2.get(self.slots[el_2]) is False:
                    set3.put(self.slots[el_2])
                    self.slots[el_2] = None
                    counter += 1
                    continue
        # проверка на наличее минимум одного элемента пересечения
        if counter == 0:
            return None
        # создание хэш-таблицы только со всеми элементами
        if counter // 10 < 2:
            step_union = 1
        if counter // 10 >= 2:
            step_union = counter // 10
        set4 = PowerSet(counter, step_union)
        for el_3 in range(set3.size()):
            if set3.slots[el_3] is not None:
                set4.put(set3.slots[el_3])
        return set4

    def issubset(
        self, set2
    ):  # возвращает True, если set2 есть подмножество текущего множества, иначе False
        counter_0 = 0  # счетчик
        counter = 0  # счетчик
        for el in range(set2.size()):  # подсчет элементов множества set2
            if set2.slots[el] is not None:
                counter_0 += 1
        for el_1 in range(
            set2.size()
        ):  # подсчет совпадений элементов текущего множества и множества set2
            if set2.slots[el_1] is not None and self.get(set2.slots[el_1]) is True:
                counter += 1
        if counter_0 == counter:  # сравнение элементов множества set2 и совпадений
            # элементов текущего множества и множества set2
            return True
        return False
