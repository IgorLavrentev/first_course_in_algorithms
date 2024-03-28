import ctypes


class DynArray:

    def __init__(self):
        self.count = 0  # текущее количество элементов в массиве
        self.capacity = 16  # текущая ёмкость буфера
        self.array = self.make_array(
            self.capacity
        )  # указатель на блок памяти нужной ёмкости, хранящий элементы PyObject

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError("Index is out of bounds")
        return self.array[i]

    # увеличение емкости буфера и перезапись массива в новый массив
    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        # сравнивание текущего количества элементов в массиве и текущей емкости буфера
        if self.count == self.capacity:
            self.resize(2 * self.capacity) # увеличение текущей ёмкости буфера в 2 раза
        self.array[self.count] = itm # добавление элемента в массив
        self.count += 1 # увеличение текущего количества элементов в массиве на +1

    # добавляем объект itm в позицию i, начиная с 0
    def insert(self, i, itm):
        # если индекс i лежит вне допустимых границ, исключение
        if i < 0 or i > self.count:
            raise IndexError("Index is out of bounds")
        # сравнивание текущего количества элементов в массиве и текущей емкости буфера
        if self.count == self.capacity:
            self.resize(2 * self.capacity) # увеличение текущей емкости буфера в 2 раза
        if i == self.count:
            self.array[self.count] = itm
            self.count += 1 # увеличение текущего количества элементов в массиве на +1
            return
        for el in range(self.count - 1, i - 1, - 1):
            self.array[el + 1] = self.array[el]
        self.array[i] = itm
        self.count += 1 # увеличение текущего количества элементов в массиве на +1
        return

    # удаляем объект в позиции i
    def delete(self, i):
        # если индекс i лежит вне допустимых границ, исключение
        if i < 0 or i >= self.count:
            raise IndexError("Index is out of bounds")
        # удаление i-го элемента
        new_array = self.make_array(self.capacity)
        for el_1 in range(i):
            new_array[el_1] = self.array[el_1]
        for el_2 in range(i, self.count - 1):
            new_array[el_2] = self.array[el_2 + 1]
        self.array = new_array
        self.count -= 1 # уменьшение текущего количества элементов в массиве на -1
        # проверка необходимости уменьшения массива
        # сравнивание текущего количества элементов в массиве и половины текущей ёмкости буфера
        if self.count < (self.capacity / 2):
            if self.capacity/1.5 > 16:
                new_array = self.make_array(int(self.capacity/1.5))
            if self.capacity/1.5 <= 16:
                new_array = self.make_array(16)
            for j in range(self.count):
                new_array[j] = self.array[j]
            self.array = new_array
            if self.capacity/1.5 > 16:
                self.capacity = int(self.capacity/1.5)
            if self.capacity/1.5 <= 16:
                self.capacity = 16
