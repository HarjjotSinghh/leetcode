from typing import List


# My Solution
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        prevSmallest, prevGreatest = arrays[0][0], arrays[0][-1]
        output = 0
        for i in range(1, len(arrays)):
            smallest, greatest = arrays[i][0], arrays[i][-1]
            output = max(output, prevGreatest - smallest, greatest - prevSmallest)
            prevSmallest = min(prevSmallest, smallest)
            prevGreatest = max(prevGreatest, greatest)
        return output

# Best / Most Optimal Solution
class Solution2:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mn1, mn2 = float('inf'), float('inf')
        mx1, mx2 = float('-inf'), float('-inf')
        for i in arrays:
            mn, mx = i[0], i[-1]
            if mn < mn1:
                mn2, mn1 = mn1, mn
            elif mn < mn2:
                mn2 = mn
            if mx > mx1:
                mx2, mx1 = mx1, mx
            elif mx > mx2:
                mx2 = mx
        if mx1 == mx2 or mn1 == mn2:
            return mx1 - mn1
        for i in arrays:
            if (i[0], i[-1]) == (mn1, mx1):
                return max(abs(mx2 - mn1), abs(mx1 - mn2))
        return mx1 - mn1
