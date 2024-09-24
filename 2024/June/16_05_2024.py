from typing import List

# My Solution
class Solution:
    def minPatches(self, nums, n):
        ans = 0
        sum_val = 1
        m = len(nums)
        i = 0
        while sum_val <= n:
            if i < m and nums[i] <= sum_val:
                sum_val += nums[i]
                i += 1
            else:
                sum_val += sum_val
                ans += 1
        return ans
    
# Most Optimal Solution
class Solution2:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        i = 0
        miss = 1
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1
        return patches