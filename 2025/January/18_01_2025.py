import heapq
from typing import List
from collections import deque


# My Solution
class Solution:
    _dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def minCost(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        pq = [(0, 0, 0)]
        min_cost = [[float("inf")] * num_cols for _ in range(num_rows)]
        min_cost[0][0] = 0
        while pq:
            cost, row, col = heapq.heappop(pq)
            if min_cost[row][col] != cost:
                continue
            for d, (dx, dy) in enumerate(self._dirs):
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                    new_cost = cost + (d != (grid[row][col] - 1))
                    if min_cost[new_row][new_col] > new_cost:
                        min_cost[new_row][new_col] = new_cost
                        heapq.heappush(pq, (new_cost, new_row, new_col))
        return min_cost[num_rows - 1][num_cols - 1]


# Best / Most Optimal Solution
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dp = [[-1] * n for _ in range(m)]
        q = deque()

        def dfs(i: int, j: int, cost: int) -> None:
            if i < 0 or i == m or j < 0 or j == n:
                return
            if dp[i][j] != -1:
                return
            dp[i][j] = cost
            q.append((i, j))
            dx, dy = dirs[grid[i][j] - 1]
            dfs(i + dx, j + dy, cost)

        dfs(0, 0, 0)
        cost = 0
        while q:
            cost += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for dx, dy in dirs:
                    dfs(i + dx, j + dy, cost)
        return dp[-1][-1]
