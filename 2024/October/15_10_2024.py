
# My Solution
class Solution:
    def minimumSteps(self, s: str) -> int:
        total_swaps = 0
        black_ball_count = 0
        for char in s:
            if char == "0":
                total_swaps += black_ball_count
            else:
                black_ball_count += 1
        return total_swaps

# Best / Most Optimal Solution
class Solution2:
    def minimumSteps(self, s: str) -> int:
        res, swaps = 0, 0
        for ch in s:
            if ch == '1':
                swaps += 1
            else:
                res += swaps
        return res     
