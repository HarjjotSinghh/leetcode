from typing import List
from sys import stdin
from json import loads

# My Solution
class Solution:

    def lexicalOrder(self, n: int) -> List[int]:
        lexicographical_numbers = []
        current_number = 1
        for _ in range(n):
            lexicographical_numbers.append(current_number)
            if current_number * 10 <= n:
                current_number *= 10
            else:
                while current_number % 10 == 9 or current_number >= n:
                    current_number //= 10
                current_number += 1
        return lexicographical_numbers

# Best / Most Optimal Solution
class Solution2:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1, n + 1), key=str)
with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        print(str(Solution2().lexicalOrder(nums)).replace(" ", ""), file=f)
exit(0)
