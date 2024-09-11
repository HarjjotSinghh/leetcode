
# My Solution
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_result = start ^ goal
        count = 0
        while xor_result:
            xor_result &= xor_result - 1
            count += 1
        return count

# Best / Most Optimal Solution
class Solution2:
    def minBitFlips(self, start: int, goal: int) -> int:
        c = 0
        while start or goal:
            if start%2 != goal%2:
                c+=1
            start = start//2
            goal = goal//2
        return c
