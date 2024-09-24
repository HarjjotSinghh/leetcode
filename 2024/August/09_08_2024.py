from typing import List

# My Solution
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        for row in range(m - 2):
            for col in range(n - 2):
                if self._isMagicSquare(grid, row, col):
                    ans += 1
        return ans
    def _isMagicSquare(self, grid, row, col):
        sequence = "2943816729438167"
        sequenceReversed = "7618349276183492"
        border = []
        borderIndices = [0, 1, 2, 5, 8, 7, 6, 3]
        for i in borderIndices:
            num = grid[row + i // 3][col + (i % 3)]
            border.append(str(num))
        borderConverted = "".join(border)
        return (
            grid[row][col] % 2 == 0
            and (
                sequence.find(borderConverted) != -1
                or sequenceReversed.find(borderConverted) != -1
            )
            and grid[row + 1][col + 1] == 5
        )

# Best / Most Optimal Solution
class Solution2:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        ans = 0
        for i in range(0, row -3 + 1):
            for j in range(0, column - 3 + 1):
                if {grid[i+k][j+l] for k in range(3) for l in range(3)} != {i for i in range(1, 10)}:
                    continue
                okay = True
                sm = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != sm:
                    continue
                if grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2] != sm:
                    continue
                for k in range(3):
                    temp = 0
                    for l in range(3):
                        temp += grid[i + l][j] 
                    if  temp != sm:
                        okay = False
                        break
                    temp = 0
                    for l in range(3):
                        temp += grid[i][j + l] 
                    if  temp != sm:
                        okay = False
                        break
                if okay:
                    ans += 1
        return ans