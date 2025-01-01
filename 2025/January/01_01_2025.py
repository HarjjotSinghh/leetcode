# My Solution
class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        zeros = 0
        ans = 0
        for i in range(len(s) - 1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1
            ans = max(ans, zeros + ones)
        return ans


# Best / Most Optimal Solution
class Solution2:
    def maxScore(self, s: str) -> int:
        left = 0
        right = 0
        ans = 0
        for i in range(len(s)):
            right += 0 if s[i] == "0" else 1
        for i in range(len(s) - 1):
            left += 1 if s[i] == "0" else 0
            right += 0 if s[i] == "0" else -1
            ans = max(left + right, ans)
        return ans
