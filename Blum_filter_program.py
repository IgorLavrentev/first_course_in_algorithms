class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len  # creating a bit array of length f_len
        self.bloom_array = 1 << f_len + 1  # creating an array of bits

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
        self.bloom_array = self.set_bit(self.bloom_array, self.hash1(str1), True)
        self.bloom_array = self.set_bit(self.bloom_array, self.hash2(str1), True)

    def set_bit(self, v, index, set_bit):
        mask = 1 << index  # mask with a single bit 1
        v &= ~mask  # clear this bit in the value of v - set it to 0
        if set_bit:
            v |= mask  # if this bit needs to be set to 1
        return v

    def removing(self, str1):  # removing the i-th bit
        self.bloom_array = self.set_bit(self.bloom_array, self.hash1(str1), False)
        self.bloom_array = self.set_bit(self.bloom_array, self.hash2(str1), False)

    def is_value(self, str1):  # checking whether the string str1 is in the filter
        mask = 1 << self.hash1(str1)
        if self.bloom_array & mask:
            return True
        return False
