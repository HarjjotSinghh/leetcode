from collections import deque
from typing import List

# My Solution
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices.copy()
        stack = deque()
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                result[stack.pop()] -= prices[i]
            stack.append(i)
        return result

# Best / Most Optimal Solution
class Solution2:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = prices[:]
        for i , price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                ans[stack.pop()]-= price
            stack.append(i)
        return ans
