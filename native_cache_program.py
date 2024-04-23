class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size  # stores values
        self.values = [None] * self.size  # stores the keys
        self.hits = [0] * self.size  # stores the corresponding number of hits

    def hash_fun(self, key):
        # hash function for filling an array
        if len(key) > self.size or len(key) < 0:
            return None
        remainder = len(key.encode()) % self.size
        ind = remainder
        st = int(self.size / 5)
        # if the hash function is None
        if ind is None:
            return None
        # if the slot is empty, we return the index of the slot
        if self.slots[ind] is None:
            return ind
        # dealing with collisions
        for _ in range(10):
            if st == 0 or st < 0:
                self.displacement()
                st = int(self.size / 2)
            # the part of the hash table to the right of the index
            for i in range(ind, len(self.slots), st):
                # if the slot is empty, we return the index i
                if self.slots[i] is None:
                    return i
            # часть хэш-таблицы слева от индекса
            for j in range((len(self.slots) - ind) % st, ind, st):
                # if the slot is empty, we return the index j
                if self.slots[j] is None:
                    return j
            st -= 1
        return None

    def is_key(self, key):  # checking whether there is such a key in the slots
        for k in range(len(self.values)):
            if self.values[k] is key:
                self.hits[k] += 1
                return True
        return False

    def put(self, key, value):
        for v in range(len(self.values)):  # finding the key index in the key array
            if self.values[v] == key:
                index_key = v
        if self.is_key(key) is True:  # checking that there is no such key in the key array
            self.slots[index_key] = value  # changing the value
            return self.slots[index_key]
        result = self.hash_fun(key)
        if result is None:
            return None
        self.slots[result] = value  # adding a value to the array of values
        self.values[result] = key  # adding a value to the key array
        return self.slots[result]

    def get(self, key):  # searching and extracting a value by key
        for h in range(len(self.values)):
            if self.values[h] == key:
                val = self.slots[h]
                self.values[h] = None
                self.slots[h] = None
                self.hits[h] = 0
                return val
        return None  # return None if the key is not found

    def displacement(self):  # displacement of an element
        # finding the element with the minimum number of self.hits hits
        minimum_value = self.hits[0]
        index_minimum_value = 0
        for i in range(len(self.hits)):
            if self.hits[i] < minimum_value:
                minimum_value = self.hits[i]
                index_minimum_value = i
        # deleting an item with a minimum number of hits
        self.values[index_minimum_value] = None
        self.slots[index_minimum_value] = None
        self.hits[index_minimum_value] = 0
