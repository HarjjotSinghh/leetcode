# My Solution
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26
        for i in range(len(s)):
            curr = ord(s[i]) - ord("a")
            if first[curr] == -1:
                first[curr] = i
            last[curr] = i
        ans = 0
        for i in range(26):
            if first[i] == -1:
                continue
            between = set()
            for j in range(first[i] + 1, last[i]):
                between.add(s[j])
            ans += len(between)
        return ans


# Best / Most Optimal Solution
class Solution2:
    def countPalindromicSubsequence(self, s):
        c = "abcdefghijklmnopqrstuvwxyz"
        a, t = 0, 0
        for x in c:
            l = s.find(x)
            if l == -1:
                continue
            r = s.rfind(x)
            if l >= r:
                continue
            v = [False] * 128
            t = 0
            for i in range(l + 1, r):
                if not v[ord(s[i])]:
                    v[ord(s[i])] = True
                    t += 1
                    if t == 26:
                        break
            a += t
        return a
