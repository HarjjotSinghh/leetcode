from typing import List

# My Solution
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        freq = {}
        for row in grid:
            for num in row:
                freq[num] = freq.get(num, 0) + 1
        for num in range(1, n * n + 1):
            if num not in freq:
                missing = num
            elif freq[num] == 2:
                repeat = num
        return [repeat, missing]

# Best / Most Optimal Solution
class Solution2:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        currSum = (n*n)*((n*n) +1)//2
        seen = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in seen:
                    seen.add(grid[i][j])
                    currSum -= grid[i][j]
                else:
                    dup = grid[i][j]
        return [dup, currSum]
