from heapq import heapify, heappop, heappush
from typing import List

# My Solution
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int):
        pq = [(val, i) for i, val in enumerate(nums)]
        heapify(pq)
        for _ in range(k):
            _, i = heappop(pq)
            nums[i] *= multiplier
            heappush(pq, (nums[i], i))
        return nums

# Best / Most Optimal Solution
class Solution2:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            idx = nums.index(min(nums))
            nums[idx] *= multiplier
        return nums
