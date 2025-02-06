from collections import Counter
from itertools import combinations
from math import comb
from typing import List


# My Solution
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_counts = Counter(a * b for a, b in combinations(nums, 2)).values()
        return 8 * sum(comb(C, 2) for C in product_counts)


# Best / Most Optimal Solution
class Solution2:
    def tupleSameProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = 0
        prods = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prod = nums[i] * nums[j]
                if prod in prods:
                    ans += prods[prod]
                    prods[prod] += 1
                else:
                    prods[prod] = 1
        return ans * 8
