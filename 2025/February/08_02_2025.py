from collections import defaultdict
import heapq


# My Solution
class NumberContainers:
    def __init__(self):
        self.number_to_indices = defaultdict(list)
        self.index_to_numbers = {}

    def change(self, index: int, number: int) -> None:
        self.index_to_numbers[index] = number
        heapq.heappush(self.number_to_indices[number], index)

    def find(self, number: int) -> int:
        if not self.number_to_indices[number]:
            return -1
        while self.number_to_indices[number]:
            index = self.number_to_indices[number][0]
            if self.index_to_numbers.get(index) == number:
                return index
            heapq.heappop(self.number_to_indices[number])
        return -1


# Best / Most Optimal Solution
class NumberContainers2:
    def __init__(self):
        self.index_val = {}
        self.val_index = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.index_val[index] = number
        heapq.heappush(self.val_index[number], index)

    def find(self, number: int) -> int:
        h = self.val_index[number]
        while h and self.index_val[h[0]] != number:
            heapq.heappop(h)
        return h[0] if h else -1
