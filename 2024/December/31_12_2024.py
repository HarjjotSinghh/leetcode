from typing import List
from functools import cache


# My Solution
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        tickets: List[int] = [1, 7, 30]

        @cache
        def next_idx(curr: int, tick: int = 0) -> int:
            for i in range(curr, -1, -1):
                if days[i] <= days[curr] - tick:
                    return i
            return -1

        @cache
        def dp(i: int) -> int:
            if i < 0:
                return 0
            elif i == 0:
                return min(costs)
            return min(c + dp(next_idx(i, tickets[j])) for j, c in enumerate(costs))

        return dp(len(days) - 1)


# Best / Most Optimal Solution
class Solution2:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        traveldays = set(days)
        dp = [0] * 366
        for i in range(1, 366):
            if i not in traveldays:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(
                    dp[i - 1] + costs[0],
                    dp[i - 7] + costs[1] if i >= 7 else costs[1],
                    dp[i - 30] + costs[2] if i >= 30 else costs[2],
                )
        return dp[-1]
