import re
from fractions import Fraction

# My Solution
class Solution:
    def fractionAddition(self, expression: str) -> str:
        num = 0
        denom = 1
        nums = re.split("/|(?=[-+])", expression)
        nums = list(filter(None, nums))
        for i in range(0, len(nums), 2):
            curr_num = int(nums[i])
            curr_denom = int(nums[i + 1])
            num = num * curr_denom + curr_num * denom
            denom = denom * curr_denom
        gcd = abs(self._find_gcd(num, denom))
        num //= gcd
        denom //= gcd
        return str(num) + "/" + str(denom)
    def _find_gcd(self, a: int, b: int) -> int:
        if a == 0:
            return b
        return self._find_gcd(b % a, a)

# Best / Most Optimal Solution
class Solution2:
    def fractionAddition(self, expression: str) -> str:
        fractions = re.findall(r'[+-]?\d+/\d+', expression)
        print(fractions)
        result = Fraction(0, 1)
        for frac in fractions:
            result += Fraction(frac)
        numerator = result.numerator
        denominator = result.denominator
        return f"{numerator}/{denominator}"