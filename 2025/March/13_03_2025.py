from typing import List

# My Solution
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        total_sum = 0
        k = 0
        difference_array = [0] * (n + 1)
        for index in range(n):
            while total_sum + difference_array[index] < nums[index]:
                k += 1
                if k > len(queries):
                    return -1
                left, right, val = queries[k - 1]
                if right >= index:
                    difference_array[max(left, index)] += val
                    difference_array[right + 1] -= val
            total_sum += difference_array[index]
        return k

# Best / Most Optimal Solution
class Solution2:
    def minZeroArray(self, a: List[int], queries: List[List[int]]) -> int:
        n = len(a)
        m = len(queries)
        delta = [0] * (n+1)
        q = queries[::-1]
        cur = 0
        for i,x in enumerate(a):
            cur += delta[i]
            while q and cur < x:
                l,r,height = q.pop()
                if r >= i:
                    if l > i:
                        delta[l] += height
                    else:
                        cur += height
                    delta[r+1] -= height
            if cur < x:
                return -1
        return m - len(q)
