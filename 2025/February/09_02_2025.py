from typing import List
from itertools import starmap
from collections import Counter
from operator import sub


# My Solution
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        bad_pairs = 0
        diff_count = {}
        for pos in range(len(nums)):
            diff = pos - nums[pos]
            good_pairs_count = diff_count.get(diff, 0)
            bad_pairs += pos - good_pairs_count
            diff_count[diff] = good_pairs_count + 1
        return bad_pairs


# Best / Most Optimal Solution
class Solution2:
    def countBadPairs(self, l: List[int]) -> int:
        return (((len(l) << 1) - 1) ** 2 - 1 >> 3) - (
            sum(
                v * (v - 1)
                for v in Counter(starmap(sub, enumerate(l))).values()
                if v > 1
            )
            >> 1
        )
