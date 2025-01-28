from typing import List


# My Solution
class Solution:
    def count_fishes(self, grid, visited, row, col):
        num_rows = len(grid)
        num_cols = len(grid[0])
        fish_count = 0
        q = [(row, col)]
        visited[row][col] = True
        row_directions = [0, 0, 1, -1]
        col_directions = [1, -1, 0, 0]
        while q:
            row, col = q.pop(0)
            fish_count += grid[row][col]
            for i in range(4):
                new_row = row + row_directions[i]
                new_col = col + col_directions[i]
                if (
                    0 <= new_row < num_rows
                    and 0 <= new_col < num_cols
                    and grid[new_row][new_col]
                    and not visited[new_row][new_col]
                ):
                    q.append((new_row, new_col))
                    visited[new_row][new_col] = True
        return fish_count

    def findMaxFish(self, grid):
        num_rows = len(grid)
        num_cols = len(grid[0])
        result = 0
        visited = [[False] * num_cols for _ in range(num_rows)]
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] and not visited[i][j]:
                    result = max(result, self.count_fishes(grid, visited, i, j))
        return result


# Best / Most Optimal Solution
class Solution2:
    def dfs(self, grid, i, j):
        nrow, ncol = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= nrow or j >= ncol:
            return 0
        if grid[i][j] == 0:
            return 0
        temp = grid[i][j]
        grid[i][j] = 0
        return (
            temp
            + self.dfs(grid, i + 1, j)
            + self.dfs(grid, i - 1, j)
            + self.dfs(grid, i, j + 1)
            + self.dfs(grid, i, j - 1)
        )

    def findMaxFish(self, grid: List[List[int]]) -> int:
        res = 0
        nrow, ncol = len(grid), len(grid[0])
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] != 0:
                    res = max(res, self.dfs(grid, i, j))
        return res
