
# My Solution
class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + n * (n - 1) * 2


# Best / Most Optimal Solution
class Solution2:
    def coloredCells(self, n: int) -> int:
        return 2*n*(n-1)+1
