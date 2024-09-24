import itertools

# My Solution
class Solution:
    def strangePrinter(self, s: str) -> int:
        s = "".join(char for char, _ in itertools.groupby(s))
        memo = {}
        def _minimum_turns(start, end) -> int:
            if start > end:
                return 0
            if (start, end) in memo:
                return memo[(start, end)]
            min_turns = 1 + _minimum_turns(start + 1, end)
            for k in range(start + 1, end + 1):
                if s[k] == s[start]:
                    turns_with_match = _minimum_turns(
                        start, k - 1
                    ) + _minimum_turns(k + 1, end)
                    min_turns = min(min_turns, turns_with_match)
            memo[(start, end)] = min_turns
            return min_turns
        return _minimum_turns(0, len(s) - 1)

# Best / Most Optimal Solution
class Solution2:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        a = [s[0]]
        for i in range(1, n):
            if s[i] != s[i - 1]:
                a.append(s[i])
        n = len(a)
        h = {}
        t = [n] * n
        for i in reversed(range(n)):
            if a[i] in h:
                t[i] = h[a[i]]
            h[a[i]] = i
        d = [[0] * n for _ in range(n + 1)]
        for i in range(n):
            d[i][i] = 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                d[i][j] = 1 + d[i + 1][j]
                k = t[i]
                while k <= j:
                    d[i][j] = min(d[i][j], d[i][k - 1] + d[k + 1][j])
                    k = t[k]
        return d[0][n - 1]
