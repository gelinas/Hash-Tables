class DynamicArray:
    # my_array = [4]
    def __init__ (self, capacity):
        self.capacity = capacity
        # simulate array length tracking
        self.count = 0
        # simulate array memory allocation for purposes of exercise using memory in Python list
        self.storage = [None] * self.capacity

    def insert(self, index, value):
        # adding another item
        # ensure open space exists for another item
        if self.count >= self.capacity:
            # TODO: make array dynamically resize
            # print("Error: array is full")
            # return
            self.double_size()

        # ensure index is in range
        if index > self.count:
            print("Error: index is out of range")
            return

        # if both conditions met, shift everything over to right, insert out value
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]
        self.storage[index] = value
        self.count += 1

    def append(self, value):
        self.insert(self.count, value)

    def double_size(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage

my_array = DynamicArray(4)
print(my_array.storage) # [None, None, None, None] emulation of allocated memeory
my_array.insert(0, 1) # [1, None, None, None]
my_array.insert(0, 2) # [2, 1, None, None]
my_array.insert(1, 3) # [2, 3, 1, None]
my_array.insert(3, 4) # [2, 3, 1, 4]
my_array.insert(0, 5) # Error: not enough space before double_size implemented
# [5, 2, 3, 1, 4, None, None, None] after implement double size 

print(my_array.storage)