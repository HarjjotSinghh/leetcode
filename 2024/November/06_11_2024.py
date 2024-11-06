from typing import List


# My Solution
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        values = nums.copy()
        for i in range(n):
            for j in range(n - i - 1):
                if values[j] <= values[j + 1]:
                    continue
                else:
                    if bin(values[j]).count("1") == bin(values[j + 1]).count("1"):
                        values[j], values[j + 1] = values[j + 1], values[j]
                    else:
                        return False
        return True


# Best / Most Optimal Solution
class Solution3:
    def canSortArray(self, nums: List[int]) -> bool:
        groups = []
        curr = []
        currBits = None
        for num in nums:
            if not currBits:
                currBits = num.bit_count()
            if num.bit_count() == currBits:
                curr.append(num)
            else:
                currBits = num.bit_count()
                groups.append(curr)
                curr = [num]
        if curr:
            groups.append(curr)

        out = []
        for g in groups:
            out += sorted(g)
        return out == sorted(nums)
