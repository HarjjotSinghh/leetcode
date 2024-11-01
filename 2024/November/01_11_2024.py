# My Solution
class Solution:
    def makeFancyString(self, s: str) -> str:
        prev = s[0]
        frequency = 1
        ans = s[0]
        for i in range(1, len(s)):
            if s[i] == prev:
                frequency += 1
            else:
                prev = s[i]
                frequency = 1
            if frequency < 3:
                ans += s[i]
        return ans


# Best / Most Optimal Solution
class Solution2:
    def makeFancyString(self, s: str) -> str:
        ret = []
        cnt = 1
        prev = None
        for c in s:
            if c == prev:
                cnt += 1
            else:
                cnt = 1
            prev = c
            if cnt < 3:
                ret.append(c)
        return "".join(ret)
