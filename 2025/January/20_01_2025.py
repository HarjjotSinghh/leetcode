from typing import List


# My Solution
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        num_rows, num_cols = len(mat), len(mat[0])
        row_count, col_count = [0] * num_rows, [0] * num_cols
        num_to_pos = {}
        for row in range(num_rows):
            for col in range(num_cols):
                num_to_pos[mat[row][col]] = [row, col]
        for i in range(len(arr)):
            num = arr[i]
            row, col = num_to_pos[num]
            row_count[row] += 1
            col_count[col] += 1
            if row_count[row] == num_cols or col_count[col] == num_rows:
                return i
        return -1


# Best / Most Optimal Solution
class Solution2:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        rows = [0] * m
        cols = [0] * n
        numToRow = [0] * (m * n + 1)
        numToCol = [0] * (m * n + 1)
        for i, row in enumerate(mat):
            for j, num in enumerate(row):
                numToRow[num] = i
                numToCol[num] = j
        for i, a in enumerate(arr):
            rows[numToRow[a]] += 1
            if rows[numToRow[a]] == n:
                return i
            cols[numToCol[a]] += 1
            if cols[numToCol[a]] == m:
                return i
