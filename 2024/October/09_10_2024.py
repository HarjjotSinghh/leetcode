
# My Soluiton
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        min_adds_required = 0
        for c in s:
            if c == "(":
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    min_adds_required += 1
        return min_adds_required + open_brackets

# Best / Most Optimal Solution
class Solution2:
    def minAddToMakeValid(self, s: str) -> int:
        need = 0
        res = 0
        for p in s:
            if p == '(':
                need += 1
            if p == ')':
                need -= 1
                if need == -1:
                    res += 1
                    need = 0
        return res + need
