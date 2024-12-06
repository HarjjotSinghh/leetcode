from typing import List


# My Solution
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        count = 0
        for num in range(1, n + 1):
            if num in banned_set:
                continue
            if maxSum - num < 0:
                return count
            maxSum -= num
            count += 1
        return count


# Best / Most Optimal Solution
class Solution2:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ans = 0
        temp = 0
        banned = set(banned)
        for i in range(1, n + 1):
            if temp >= maxSum or temp + i > maxSum:
                break
            elif i not in banned:
                temp += i
                ans += 1
        return ans
