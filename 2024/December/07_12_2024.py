from typing import List
import math

# My Solution
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canAchievePenalty(penalty):
            operations = 0
            for balls in nums:
                if balls > penalty:
                    operations += (balls - 1) // penalty
            return operations <= maxOperations
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if canAchievePenalty(mid):
                right = mid
            else:
                left = mid + 1
        return left

# Best / Most Optimal Solution
class Solution2:
    def minimumSize(self, nums: List[int], O: int) -> int:
        N = len(nums)
        S = sum(nums)
        G = N+O
        if G >= S: return 1
        def verify(v):
            return sum(math.ceil(n/v) for n in nums) <= G
        l = math.ceil(S/G)-1
        h = min(max(nums),math.floor(S/O))
        while l<h-1:
            m = (h+l)//2
            if verify(m): h=m
            else: l=m
        return h
