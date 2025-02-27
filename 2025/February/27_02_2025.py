from typing import List
from collections import defaultdict

# My Solution
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        num_set = set(arr)
        max_len = 0
        n = len(arr)
        for start in range(n):
            for next in range(start + 1, n):
                prev = arr[next]
                curr = arr[start] + arr[next]
                curr_len = 2
                while curr in num_set:
                    prev, curr = curr, curr + prev
                    curr_len += 1
                    max_len = max(max_len, curr_len)
        return max_len

# Best / Most Optimal Solution
class Solution2:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        lookup = {}
        res = 0
        for pos, num in enumerate(arr):
            lookup[num] = defaultdict(lambda: 2)
            for prev_pos in range(pos - 1, -1, -1):
                prev = arr[prev_pos]
                prev2 = num - prev
                if prev2 >= prev:
                    break
                if prev2 not in lookup:
                    continue
                lookup[num][prev] = lookup[prev][prev2] + 1
                res = max(res, lookup[num][prev])
        return res