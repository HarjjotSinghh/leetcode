from typing import List


# My Solution
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        lastParity = nums[0] % 2
        for num in nums[1:]:
            parity = num % 2
            if parity == lastParity:
                return False
            else:
                lastParity = parity
        return True


# Best / Most Optimal Solution
class Solution2:
    def isArraySpecial(self, nums: List[int]) -> bool:
        lastParity = nums[0] % 2
        for num in nums[1:]:
            parity = num % 2
            if parity == lastParity:
                return False
            else:
                lastParity = parity
        return True
