from typing import List
from itertools import accumulate


# My Solution
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_prefix_sum = 0
        max_prefix_sum = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            min_prefix_sum = min(min_prefix_sum, prefix_sum)
            max_prefix_sum = max(max_prefix_sum, prefix_sum)
        return max_prefix_sum - min_prefix_sum

# Best / Most Optimal Solution
class Solution2:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        s = list(accumulate(nums, initial=0))
        return max(s) - min(s)
