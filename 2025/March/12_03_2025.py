from bisect import bisect_left
from typing import List

# My Solution
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positive = 0
        negative = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            if nums[i] > 0:
                positive += 1
            else:
                negative += 1
        return max(positive, negative)

# Best / Most Optimal Solution
class Solution2:
    def maximumCount(self, nums: List[int]) -> int:
        first_non_negative = bisect_left(nums, 0)
        first_positive = bisect_left(nums, 1)
        neg = first_non_negative
        pos = len(nums) - first_positive
        return max(neg,pos)
