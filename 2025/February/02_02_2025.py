from typing import List


# My Solution
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        inversion_count = 0
        for index in range(1, n):
            if nums[index] < nums[index - 1]:
                inversion_count += 1
        if nums[0] < nums[n - 1]:
            inversion_count += 1
        return inversion_count <= 1


# Best / Most Optimal Solution
class Solution2:
    def check(self, nums: List[int]) -> bool:
        sorted_nums = list(sorted(nums))
        for i in range(len(nums)):
            if sorted_nums == nums:
                return True
            sorted_nums = sorted_nums[1:] + [sorted_nums[0]]
        return False
