from itertools import pairwise
from typing import List


# My Solution
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sum_num, max_sum = nums[0], nums[0]
        for a, b in pairwise(nums):
            if b > a:
                sum_num += b
            else:
                sum_num = b
            max_sum = max(sum_num, max_sum)
        return max_sum


# Best / Most Optimal Solution
class Solution2:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = 0
        cur = nums[0]
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                cur += nums[i + 1]
            else:
                result = max(cur, result)
                cur = nums[i + 1]
        return max(cur, result)
