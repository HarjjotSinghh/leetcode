from typing import List

# My Solution
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        greater = []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)
        less.extend(equal)
        less.extend(greater)
        return less

# Best / Most Optimal Solution
class Solution2:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small = []
        big = []
        c = 0
        for i in nums:
            if i<pivot:
                small.append(i)
            elif i>pivot:
                big.append(i)
            elif i==pivot:
                c+=1
        res = []
        res += small
        res += [pivot]*c
        res += big
        return res
