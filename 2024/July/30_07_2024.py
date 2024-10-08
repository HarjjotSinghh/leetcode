# My Soluiton
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        min_deletions = 0
        b_count = 0
        for ch in s:
            if ch == "b":
                b_count += 1
            else:
                min_deletions = min(min_deletions + 1, b_count)
        return min_deletions

# Best / Most Optimal Solution
class Solution2:
    def minimumDeletions(self, s):
        ans, count = 0, 0
        for i in s:
            if i == 'b':
                count += 1
            elif count:
                ans += 1
                count -= 1
        return ans
