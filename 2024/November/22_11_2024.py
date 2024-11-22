from typing import List
from collections import Counter


# My Solution
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_frequency = {}
        for current_row in matrix:
            row_pattern = "".join(
                "T" if num == current_row[0] else "F" for num in current_row
            )
            pattern_frequency[row_pattern] = pattern_frequency.get(row_pattern, 0) + 1
        return max(pattern_frequency.values(), default=0)


# Best / Most Optimal Solution
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt = Counter()
        for row in matrix:
            t = tuple(row) if row[0] == 0 else tuple(x ^ 1 for x in row)
            cnt[t] += 1
        return max(cnt.values())
