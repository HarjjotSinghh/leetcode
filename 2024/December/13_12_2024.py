from typing import List
from collections import deque

# My Solution
class Solution:
    def findScore(self, nums: List[int]) -> int:
        stk = []
        res = 0
        for i in range(len(nums)):
            if not stk or nums[i] < stk[-1]:
                stk.append(nums[i])
            else:
                while stk:
                    res += stk.pop()
                    if stk:
                        stk.pop()
        while stk:
            res += stk.pop()
            if stk:
                stk.pop()
        return res

# Best / Most Optimal Soluion
class Solution2:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        n = len(nums)
        q = deque()
        for i in range(n):
            if q and nums[i]>=q[-1]:
                skip=False
                while q:
                    add = q.pop()
                    if not skip:
                        score += add
                    skip = not skip
                continue

            q.append(nums[i])
        skip=False
        while q:
            add = q.pop()
            if not skip:
                score += add
            skip = not skip
        return score
