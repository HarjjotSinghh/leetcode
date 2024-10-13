from collections import defaultdict
from typing import List

# My Solution
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        merged = []
        for i in range(len(nums)):
            for num in nums[i]:
                merged.append((num, i))
        merged.sort()
        freq = defaultdict(int)
        left, count = 0, 0
        range_start, range_end = 0, float("inf")
        for right in range(len(merged)):
            freq[merged[right][1]] += 1
            if freq[merged[right][1]] == 1:
                count += 1
            while count == len(nums):
                cur_range = merged[right][0] - merged[left][0]
                if cur_range < range_end - range_start:
                    range_start = merged[left][0]
                    range_end = merged[right][0]

                freq[merged[left][1]] -= 1
                if freq[merged[left][1]] == 0:
                    count -= 1
                left += 1
        return [range_start, range_end]

# Best / Most Optimial Solution
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i, evs in enumerate(nums):
            for v in evs:
                d[v].append(i)
        keys = sorted(d.keys())
        lo = 0
        n = len(nums)
        dd = defaultdict(int)
        le, ri = -1, float('Inf')
        have = 0
        for hi in range(len(keys)):
            for x in d[keys[hi]]:
                dd[x] += 1
                if dd[x] == 1:
                    have += 1
            while have == n:
                curr = keys[hi] - keys[lo]
                if ri - le > curr:
                    ri = keys[hi]
                    le = keys[lo]
                for x in d[keys[lo]]:
                    dd[x] -= 1
                    if dd[x] == 0:
                        have -= 1
                lo += 1
        return [le, ri]
