
# My Solution
class MyCircularDeque:
    def __init__(self, k):
        self.queue = [0] * k
        self.front = 0
        self.rear = k - 1
        self.size = 0
        self.capacity = k
    def insertFront(self, value):
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.queue[self.front] = value
        self.size += 1
        return True
    def insertLast(self, value):
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True
    def deleteFront(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True
    def deleteLast(self):
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True
    def getFront(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]
    def getRear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
    def isEmpty(self):
        return self.size == 0
    def isFull(self):
        return self.size == self.capacity

# Best / Most Optimal Solution
class MyCircularDeque:
    def __init__(self, k: int):
        self.queue = [0] * k
        self.front = 0
        self.rear = -1
        self.count = 0
        self.maxSize = k
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.maxSize
        self.queue[self.front] = value
        self.count += 1
        return True
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.maxSize
        self.queue[self.rear] = value 
        self.count += 1
        return True
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.maxSize
        self.count -= 1
        return True
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.maxSize
        self.count -= 1
        return True
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
    def isEmpty(self) -> bool:
        return self.count == 0
    def isFull(self) -> bool:
        return self.count == self.maxSize
