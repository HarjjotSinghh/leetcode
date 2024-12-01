from typing import List

# My Solution
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False

# Best / Most Optimal Solution
class Solution2:
    def checkIfExist(self, arr: List[int]) -> bool:
        ls=set()
        for i in arr:
            if 2*i in ls or(i%2==0 and i//2 in ls):
                return True
            ls.add(i)
        return False
