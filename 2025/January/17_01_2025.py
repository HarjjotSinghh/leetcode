from typing import List


# My Solution
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return sum(derived) % 2 == 0


# Best / Most Optimal Solution
class Solution2:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return derived.count(1) % 2 == 0
