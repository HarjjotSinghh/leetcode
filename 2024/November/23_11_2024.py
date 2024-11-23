from typing import List


# My Solution
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        result = [["." for _ in range(m)] for _ in range(n)]
        for i in range(m):
            lowest_row_with_empty_cell = n - 1
            for j in range(n - 1, -1, -1):
                if box[i][j] == "#":
                    result[lowest_row_with_empty_cell][m - i - 1] = "#"
                    lowest_row_with_empty_cell -= 1
                if box[i][j] == "*":
                    result[j][m - i - 1] = "*"
                    lowest_row_with_empty_cell = j - 1
        return result


# Best / Most Optimal Solution
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            start = len(row) - 1
            for i in range(len(row) - 1, -1, -1):
                if row[i] == "*":
                    start = i - 1
                elif row[i] == "#":
                    row[start], row[i] = row[i], row[start]
                    start -= 1
        result = zip(*box[::-1])
        return result
