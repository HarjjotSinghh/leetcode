from typing import List
import heapq

# My Solution
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k
        for num in nums:
            self.add(num)
    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k or self.min_heap[0] < val:
            heapq.heappush(self.min_heap, val)
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)
        return self.min_heap[0]

# Best / Most Optimal Solution
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.stream = nums
        self.k = k
        heapq.heapify(self.stream)
        while len(self.stream) > self.k:
            heapq.heappop(self.stream)
    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)
        while len(self.stream) > self.k:
            heapq.heappop(self.stream)
        return self.stream[0]
