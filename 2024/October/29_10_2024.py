from typing import List


# My Solution
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [[0] * 2 for _ in range(M)]
        for i in range(M):
            dp[i][0] = 1
        max_moves = 0
        for j in range(1, N):
            for i in range(M):
                if grid[i][j] > grid[i][j - 1] and dp[i][0] > 0:
                    dp[i][1] = max(dp[i][1], dp[i][0] + 1)
                if i - 1 >= 0 and grid[i][j] > grid[i - 1][j - 1] and dp[i - 1][0] > 0:
                    dp[i][1] = max(dp[i][1], dp[i - 1][0] + 1)
                if i + 1 < M and grid[i][j] > grid[i + 1][j - 1] and dp[i + 1][0] > 0:
                    dp[i][1] = max(dp[i][1], dp[i + 1][0] + 1)
                max_moves = max(max_moves, dp[i][1] - 1)
            for k in range(M):
                dp[k][0] = dp[k][1]
                dp[k][1] = 0
        return max_moves


# Best / Most Optimal Solution
class Solution2:
    def maxMoves(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        start_col = [True] * num_rows
        goto_col = [False] * num_rows
        for col_idx in range(num_cols - 1):
            for row_idx in range(num_rows):
                if not start_col[row_idx]:
                    continue
                if row_idx > 0:
                    goto_col[row_idx - 1] |= (
                        grid[row_idx - 1][col_idx + 1] > grid[row_idx][col_idx]
                    )
                if row_idx + 1 < num_rows:
                    goto_col[row_idx + 1] |= (
                        grid[row_idx + 1][col_idx + 1] > grid[row_idx][col_idx]
                    )
                goto_col[row_idx] |= grid[row_idx][col_idx + 1] > grid[row_idx][col_idx]
            if not any(goto_col):
                return col_idx
            start_col = goto_col
            goto_col = [False] * num_rows
        else:
            return col_idx + 1 if any(start_col) else col_idx
