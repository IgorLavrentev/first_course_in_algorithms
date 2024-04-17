class PowerSet:

    def __init__(self):  # реализация хранилища
        self.powerset = []

    def size(self):  # количество элементов в множестве
        return len(self.powerset)

    def put(self, value):
        if value not in self.powerset:
            self.powerset.append(value)
        return value

    def get(self, value):  # возвращает True если value имеется в множестве, иначе False
        if value in self.powerset:
            return True
        return False

    def remove(self, value):  # возвращает True если value удалено, иначе False
        for i in range(len(self.powerset)):
            if self.powerset[i] == value:
                del self.powerset[i]
                return True
        return False

    def intersection(self, set2):  # пересечение текущего множества и set2
        set3 = PowerSet()
        for i in range(len(self.powerset)):
            if set2.get(self.powerset[i]):
                set3.put(self.powerset[i])
        if set3.size() != 0:
            return set3
        return None

    def union(self, set2):  # объединение текущего множества и set2
        set3 = PowerSet()
        for i in range(len(self.powerset)):  # добавление элементов из первого множества
            set3.put(self.powerset[i])
        for j in range(set2.size()):  # добавление элементов из второго множества
            if set2.sequence_number(j) not in self.powerset:
                set3.put(set2.sequence_number(j))
        if set3.size() >= len(self.powerset):
            return set3
        return None

    def difference(self, set2):  # разница текущего множества и set2
        set3 = PowerSet()
        for i in range(len(self.powerset)):
            if set2.get(self.powerset[i]):
                continue
            set3.put(self.powerset[i])
        if set3.size() > 0:
            return set3
        return None

    # возвращает True, если set2 есть подмножество текущего множества, иначе False
    def issubset(self, set2):
        counter = 0
        for i in range(len(self.powerset)):
            if set2.get(self.powerset[i]):
                counter += 1
        if counter == set2.size():
            return True
        return False

    def sequence_number(self, k): # метод возвращения k-ого элемента множества
        return self.powerset[k]
