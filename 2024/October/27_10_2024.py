from typing import List


# My Solution
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        ans = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j]:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
                    ans += dp[i + 1][j + 1]
        return ans


# Best / Most Optimal Solution
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = matrix
        res = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if dp[r][c] == 0:
                    continue
                if r != 0 and c != 0:
                    if dp[r - 1][c] > 0 and dp[r][c - 1] > 0 and dp[r - 1][c - 1] > 0:
                        dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
                res += dp[r][c]
        return res
