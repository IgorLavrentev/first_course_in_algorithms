class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len  # creating a bit array of length f_len
        self.bloom_array = [0] * f_len

    def hash1(self, str1):
        code_previous = 0  # previous result
        for c in str1:
            code = code_previous * 17 + ord(c)
            code_previous = code
        return code % self.filter_len

    def hash2(self, str1):
        code_previous = 0  # previous result
        for c in str1:
            code = code_previous * 223 + ord(c)
            code_previous = code
        return code % self.filter_len

    def add(self, str1):  # adding a line str1 to the filter
        self.bloom_array[self.hash1(str1)] |= 1  # bit logical addition
        self.bloom_array[self.hash2(str1)] |= 1  # bit logical addition

    def is_value(self, str1):  # checking whether the string str1 is in the filter
        if (self.bloom_array[self.hash1(str1)] & 1) & (
            self.bloom_array[self.hash2(str1)] & 1
        ):  # bit logical multiplication
            return True
        return False
