
# My Solution
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        numeric_string = ""
        for ch in s:
            numeric_string += str(ord(ch) - ord("a") + 1)
        while k > 0:
            digit_sum = 0
            for digit in numeric_string:
                digit_sum += int(digit)
            numeric_string = str(digit_sum)
            k -= 1
        return int(numeric_string)

# Best / Most Optimal Solution
class Solution2:
    def getLucky(self, s: str, k: int) -> int:
        def convert(s):
            return ''.join(str(ord(c) - ord('a') + 1) for c in s)
        def transform(n):
            return sum(int(d) for d in str(n))
        num = convert(s)
        for _ in range(k):
            num = transform(num)
        return num
