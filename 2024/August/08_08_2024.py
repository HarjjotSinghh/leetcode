from typing import List

# My Solution
class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        traversed = []
        step = 1
        direction = 0
        while len(traversed) < rows * cols:
            for _ in range(2):
                for _ in range(step):
                    if (
                        rStart >= 0
                        and rStart < rows
                        and cStart >= 0
                        and cStart < cols
                    ):
                        traversed.append([rStart, cStart])
                    rStart += dir[direction][0]
                    cStart += dir[direction][1]
                direction = (direction + 1) % 4
            step += 1
        return traversed

# Best / Most Optimal Solution
class Solution2:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        ans = [[rStart, cStart]]
        if rows * cols == 1:
            return ans
        k = 1
        while True:
            for dr, dc, dk in [[0, 1, k], [1, 0, k], [0, -1, k + 1], [-1, 0, k + 1]]:
                for _ in range(dk):
                    rStart += dr
                    cStart += dc
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        ans.append([rStart, cStart])
                        if len(ans) == rows * cols:
                            return ans
            k += 2
