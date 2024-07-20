from typing import List

# My Solution
class Solution:
    def restoreMatrix(self, rowSum, colSum):
        N = len(rowSum)
        M = len(colSum)
        orig_matrix = [[0] * M for _ in range(N)]
        i, j = 0, 0
        while i < N and j < M:
            orig_matrix[i][j] = min(rowSum[i], colSum[j])
            rowSum[i] -= orig_matrix[i][j]
            colSum[j] -= orig_matrix[i][j]
            if rowSum[i] == 0:
                i += 1
            else:
                j += 1
        return orig_matrix

# Best / Most Optimal Solution
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        col_sum = colSum
        row_sum = rowSum
        mat = [[0]*len(col_sum) for i in range(len(row_sum))]
        i = 0
        j = 0
        while i < len(row_sum) and j < len(col_sum):
            mat[i][j] = min(row_sum[i], col_sum[j])
            if row_sum[i] == col_sum[j]:
                i += 1
                j += 1
            elif row_sum[i] > col_sum[j]:
                row_sum[i] -= col_sum[j]
                j += 1
            else:
                col_sum[j] -= row_sum[i]
                i += 1
        return mat
