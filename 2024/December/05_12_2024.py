# My Solution
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        g1 = (i for i in range(len(start)) if (start[i] != "_"))
        g2 = (j for j in range(len(target)) if (target[j] != "_"))
        l, m = next(g1, -1), next(g2, -1)
        while (l >= 0) and (m >= 0):
            if (
                (start[l] != target[m])
                or ((start[l] == "L") and (l < m))
                or ((start[l] == "R") and (l > m))
            ):
                return False
            l, m = next(g1, -1), next(g2, -1)
        return l == m


# Best / Most Optimal Solution
class Solution2:
    def canChange(self, start: str, target: str) -> bool:
        if start == target:
            return True
        need_l = 0
        store_r = 0
        for s, v in zip(start, target):
            if s == "R":
                if need_l > 0:
                    return False
                store_r += 1
            if v == "L":
                if store_r > 0:
                    return False
                need_l += 1
            if v == "R":
                if store_r == 0:
                    return False
                store_r -= 1
            if s == "L":
                if need_l == 0:
                    return False
                need_l -= 1
        return need_l == 0 and store_r == 0
