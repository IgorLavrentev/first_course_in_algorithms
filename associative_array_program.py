class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size # массив значений
        self.values = [None] * self.size # массив ключей

    def hash_fun(self, key):
        # хэш-функция для заполнения массива
        if len(key) > self.size or len(key) < 0:
            return None
        remainder = len(key.encode()) % self.size
        ind = remainder
        st = int(self.size / 5)
        # если хэш-функция равна None
        if ind is None:
            return None
        # если слот пустой - возвращаем индекс слота
        if self.slots[ind] is None:
            return ind
        # работа с коллизиями
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
        return None

    def is_key(self, key): # проверка, имеется ли в слотах такой ключ
        for k in range(len(self.values)):
            if self.values[k] is key:
                return True
        return False

    def put(self, key, value):
        for v in range(len(self.values)): # нахождение индекса ключа в массиве ключей
            if self.values[v] == key:
                index_key = v
        if self.is_key(key) is True: # проверка, что такого ключа нет в массиве ключей
            self.slots[index_key] = value # изменяем значение в таблице значений
            return
        result = self.hash_fun(key)
        if result is None:
            return None  # если из-за коллизий элемент не удаётся разместить
        self.slots[result] = value # добавляем значение в массив значений
        self.values[result] = key # добавляем значение в массив ключей
        return

    def get(self, key): # поиск и извлечение значения по ключу
        for h in range(len(self.values)):
            if self.values[h] == key:
                val = self.slots[h]
                self.values[h] = None
                self.slots[h] = None
                return val
        return None # возвращаем None, если ключ не найден
