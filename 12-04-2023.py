# Design Dynamic Array (Resizable Array)

# Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

# Your DynamicArray class should support the following operations:

# DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
# int get(int i) will return the element at index i. Assume that index i is valid.
# void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
# void pushback(int n) will push the element n to the end of the array.
# int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
# void resize() will double the capacity of the array.
# int getSize() will return the number of elements in the array.
# int getCapacity() will return the capacity of the array.
# If we call void pushback(int n) but the array is full, we should resize the array first.

# Example 1:

# Input:
# ["Array", 1, "getSize", "getCapacity"]

# Output:
# [null, 0, 1]
# Example 2:

# Input:
# ["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]

# Output:
# [null, null, 1, null, 2]
# Example 3:

# Input:
# ["Array", 1, "getSize", "getCapacity", "pushback", 1, "getSize", "getCapacity", "pushback", 2, "getSize", "getCapacity", "get", 1, "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"]

# Output:
# [null, 0, 1, null, 1, 1, null, 2, 2, 2, null, 3, 3, 1, 2]

# -------------------------------Solution---------------------------------

class DynamicArray:
    # O(n) - n = capacity
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [0] * capacity
        self.length = 0
    
    # O(1)
    def get(self, i: int) -> int:
        return self.array[i]

    # O(1)
    def insert(self, i: int, n: int) -> None:
        self.array[i] = n

    # O(1) - Avg Case / Ammortized
    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        
        self.array[self.length] = n
        self.length += 1

    # O(1)
    def popback(self) -> int:
        self.length -= 1
        return self.array[self.length]

    # O(n)
    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_array = [0] * self.capacity

        for i in range(self.length):
            new_array[i] = self.array[i]

        self.array = new_array

    # O(1)
    def getSize(self) -> int:
        return self.length

    # O(1)
    def getCapacity(self) -> int:
        return self.capacity
