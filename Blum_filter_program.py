from bitarray import bitarray


class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        # создаём битовый массив длиной f_len
        self.bloom_array = bitarray(f_len)

    def hash1(self, str1):
        code_previous = 0  # предыдущий результат
        for c in str1:
            code = code_previous * 17 + ord(c)
            code_previous = code
        return code % self.filter_len

    def hash2(self, str1):
        code_previous = 0  # предыдущий результат
        for c in str1:
            code = code_previous * 223 + ord(c)
            code_previous = code
        return code % self.filter_len

    def add(self, str1):  # добавляем строку str1 в фильтр
        self.bloom_array[self.hash1(str1)] = 1
        self.bloom_array[self.hash2(str1)] = 1

    def is_value(self, str1):  # проверка, имеется ли строка str1 в фильтре
        if (
            self.bloom_array[self.hash1(str1)] == 1
            and self.bloom_array[self.hash2(str1)] == 1
        ):
            return True
        return False
