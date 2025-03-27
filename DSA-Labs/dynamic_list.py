class DynamicList:
    def __init__(self, initial_capacity=4):
        self.capacity = initial_capacity
        self.size = 0
        self.data = [None] * self.capacity

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.data[index]

    def append(self, value):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)  # Double capacity when full
        self.data[self.size] = value
        self.size += 1

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.data[:self.size])
    


# Implementation 
dlist = DynamicList()
dlist.append(10)
dlist.append(20)
dlist.append(30)
dlist.append(40)
dlist.append(50)  # Triggers resize (capacity increases to 8)
print(dlist)  # Output: [10, 20, 30, 40, 50]
print(len(dlist))  # Output: 5
