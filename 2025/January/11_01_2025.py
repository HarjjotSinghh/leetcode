# My Solution
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        odd_count = 0
        for chr in s:
            odd_count ^= 1 << (ord(chr) - ord("a"))
        return bin(odd_count).count("1") <= k


# Best / Most Optimal Solution
class Solution2:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) == k:
            return True
        if len(s) < k:
            return False
        odd = 0
        for char in set(s):
            if s.count(char) % 2:
                odd += 1
        if odd > k:
            return False
        return True
