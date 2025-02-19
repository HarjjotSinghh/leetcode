# My Solution
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * (1 << (n - 1)):
            return ""
        first, remaining = divmod(k - 1, 1 << (n - 1))
        s = "abc"[first]
        for i in range(n - 2, -1, -1):
            idx = (remaining >> i) & 1
            s += "abc"[idx] if "abc"[idx] < s[-1] else "abc"[idx + 1]
        return s


# Best / Most Optimal Solution
class Solution2:
    def getHappyString(self, n: int, k: int) -> str:
        totalHappy = 3 * (2 ** (n - 1))
        if k > totalHappy:
            return ""
        res = ""
        choices = "abc"
        low, high = 1, totalHappy
        for _ in range(n):
            partition_size = (high - low + 1) // len(choices)
            cur = low
            for c in choices:
                if k in range(cur, cur + partition_size):
                    res += c
                    low = cur
                    high = cur + partition_size - 1
                    choices = "abc".replace(c, "")
                    break
                cur += partition_size
        return res
