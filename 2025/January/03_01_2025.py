from typing import List


# My Solution
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left_sum = right_sum = 0
        right_sum = sum(nums)
        count = 0
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum -= nums[i]
            if left_sum >= right_sum:
                count += 1
        return count


# Best / Most Optimal Solution
class Solution2:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left = 0
        right = (sum(nums) + 1) // 2
        res = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            if left >= right:
                res += 1
        return res
