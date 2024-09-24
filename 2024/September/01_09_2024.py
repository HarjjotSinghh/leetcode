from typing import List

# My Solution
class Solution:
    def construct2DArray(
        self, original: List[int], m: int, n: int
    ) -> List[List[int]]:
        if m * n != len(original):
            return []
        result_array = [[0] * n for _ in range(m)]
        for i in range(len(original)):
            result_array[i // n][i % n] = original[i]
        return result_array

# Best / Most Optimal Solution
class Solution2:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        ans = []
        for i in range(m):
            ans.append(original[i * n: (i+1) * n])
        return ans
