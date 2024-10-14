from typing import List
import heapq
import math

# My Solution
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        max_heap = [-i for i in nums]
        heapq.heapify(max_heap)
        while k > 0:
            k -= 1
            max_element = -heapq.heappop(max_heap)
            ans += max_element
            heapq.heappush(max_heap, -math.ceil(max_element / 3))
        return ans


# Best / Most Optimal Solution
class Solution2:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        ans = 0
        for i in range(k):
            ans -= heapq.heappushpop(nums, math.floor(nums[0]/3))
        return ans
