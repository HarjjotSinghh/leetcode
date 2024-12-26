from typing import List


# My Solution
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.lower_bound(nums, upper + 1) - self.lower_bound(nums, lower)

    def lower_bound(self, nums: List[int], value: int) -> int:
        left = 0
        right = nums.__len__() - 1
        result = 0
        while left < right:
            sum = nums[left] + nums[right]
            if sum < value:
                result += right - left
                left += 1
            else:
                right -= 1
        return result


# Best / Most Optimal Solution
class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        def count(t):
            i, j = 0, len(nums) - 1
            res = 0
            while i < j:
                if nums[i] + nums[j] > t:
                    j -= 1
                else:
                    res += j - i
                    i += 1
            return res

        nums.sort()
        return count(upper) - count(lower - 1)
