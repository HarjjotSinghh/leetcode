# My Solution
from itertools import pairwise
from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        ans = [[-1] * n for _ in range(m)]
        q = deque()
        for i, row in enumerate(isWater):
            for j, v in enumerate(row):
                if v:
                    q.append((i, j))
                    ans[i][j] = 0
        while q:
            i, j = q.popleft()
            for a, b in pairwise((-1, 0, 1, 0, -1)):
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and ans[x][y] == -1:
                    ans[x][y] = ans[i][j] + 1
                    q.append((x, y))
        return ans


# Best / Most Optimal Solution
class Solution2:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = deque()
        n = len(isWater[0])
        m = len(isWater)
        output = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    output[i][j] = 0
                    q.append((i, j))
        while q:
            i, j = q.popleft()
            if 0 < i < m and output[i - 1][j] == -1:
                output[i - 1][j] = output[i][j] + 1
                q.append((i - 1, j))
            if 0 < j < n and output[i][j - 1] == -1:
                output[i][j - 1] = output[i][j] + 1
                q.append((i, j - 1))
            if 0 <= j < n - 1 and output[i][j + 1] == -1:
                output[i][j + 1] = output[i][j] + 1
                q.append((i, j + 1))
            if 0 <= i < m - 1 and output[i + 1][j] == -1:
                output[i + 1][j] = output[i][j] + 1
                q.append((i + 1, j))
        return output
