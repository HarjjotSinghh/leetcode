from typing import List
from collections import Counter


# My Solution
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or_value = 0
        dp = [0] * (1 << 17)
        dp[0] = 1
        for num in nums:
            for i in range(max_or_value, -1, -1):
                dp[i | num] += dp[i]
            max_or_value |= num
        return dp[max_or_value]


# Best / Most Optimal Solution
class Solution2:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        prev = Counter()
        prev[0] = 1
        for elem in nums:
            max_or |= elem
            current = Counter()
            for prev_or, cnt in prev.items():
                current[prev_or | elem] += cnt
            prev.update(current)
        return prev[max_or]
