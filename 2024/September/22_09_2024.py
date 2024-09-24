
# My Solution
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1
        while k > 0:
            step = self._count_steps(n, curr, curr + 1)
            if step <= k:
                curr += 1
                k -= step
            else:
                curr *= 10
                k -= 1
        return curr
    def _count_steps(self, n: int, prefix1: int, prefix2: int) -> int:
        steps = 0
        while prefix1 <= n:
            steps += min(n + 1, prefix2) - prefix1
            prefix1 *= 10
            prefix2 *= 10
        return steps

# Best / Most Optimal Solution
class Solution2:
    def findKthNumber(self, n: int, k: int) -> int:
        def calc_steps(curr, n):
            steps = 0
            nxt = curr + 1
            while curr <= n:
                steps += min(n + 1, nxt) - curr
                curr *= 10
                nxt *= 10
            return steps
        curr = 1
        k -= 1
        while k > 0:
            steps = calc_steps(curr, n)
            if steps <= k:
                k -= steps
                curr += 1
            else:
                curr *= 10
                k -= 1
        return curr
