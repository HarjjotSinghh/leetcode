from typing import List
import collections

# My Solution
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dictionary_set = set(dictionary)
        dp = [0] * (len(s) + 1)
        for start in range(n - 1, -1, -1):
            dp[start] = 1 + dp[start + 1]
            for end in range(start, n):
                curr = s[start: end + 1]
                if curr in dictionary_set:
                    dp[start] = min(dp[start], dp[end + 1])
        return dp[0]

# Best / Most Optimal Solution
class Solution2:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        short = float('inf')
        book = collections.defaultdict(list)
        for w in dictionary:
            short = min(short, len(w))
            book[w[-1]].append(w)
        dp = [i for i in range(short)]
        for i in range(short, len(s)+1):
            res = dp[i-1] + 1
            for w in book[s[i-1]]:
                if len(w) > i:
                    continue
                if w == s[i-len(w):i]:
                    res = min(res, dp[i-len(w)])
            dp.append(res)
        return dp[-1]
