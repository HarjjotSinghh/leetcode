from typing import List
from itertools import pairwise


# My Solution
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_len = inc_len = dec_len = 1
        for a, b in pairwise(nums):
            inc_len = inc_len + 1 if a < b else 1
            dec_len = dec_len + 1 if a > b else 1
            max_len = max(max_len, inc_len, dec_len)
        return max_len


# Best / Most Optimal Solution
class Solution2:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        temp_count = 1
        n = len(nums)
        max_v = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                temp_count += 1
                max_v = max(temp_count, max_v)
            else:
                temp_count = 1
        temp_count = 1
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                temp_count += 1
                max_v = max(temp_count, max_v)
            else:
                temp_count = 1
        return max_v
