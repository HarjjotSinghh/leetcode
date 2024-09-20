# My Solution
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reversed_string = s[::-1]
        combined_string = s + "#" + reversed_string
        prefix_table = self._build_prefix_table(combined_string)
        palindrome_length = prefix_table[-1]
        suffix = reversed_string[: len(s) - palindrome_length]
        return suffix + s
    def _build_prefix_table(self, s: str) -> list:
        prefix_table = [0] * len(s)
        length = 0
        for i in range(1, len(s)):
            while length > 0 and s[i] != s[length]:
                length = prefix_table[length - 1]
            if s[i] == s[length]:
                length += 1
            prefix_table[i] = length
        return prefix_table

# Best / Most Optimal Solution
class Solution2:
    def shortestPalindrome(self, s: str) -> str:
        i = 0
        n = len(s)
        for j in range(n):
            if s[i] == s[n-j-1]:
                i += 1
        if i==n:
            return s
        p = s[i:n][::-1]
        return p + self.shortestPalindrome(s[:i]) + s[i:]

