from itertools import pairwise
from typing import List


# My Solution
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        trail, power = 1, [nums[0]]
        for a, b in pairwise(nums):
            trail = trail + 1 if a + 1 == b else 1
            power.append(b if trail >= k else -1)
        return power[k - 1 :]


# Best / Most Optimal Solution
class Solution2:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        ans = []
        l, r = 0, 1
        n = len(nums)
        while r < n:
            if nums[r] - nums[r - 1] != 1:
                while l < r and l + k - 1 < n:
                    ans.append(-1)
                    l += 1
                l = r
            elif r - l == k - 1:
                ans.append(nums[r])
                l += 1

            r += 1
        return ans
