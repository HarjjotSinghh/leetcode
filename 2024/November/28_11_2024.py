from collections import deque


# My Solution
class Solution:
    _directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def minimumObstacles(self, grid):
        def _is_valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        m, n = len(grid), len(grid[0])
        min_obstacles = [[float("inf")] * n for _ in range(m)]
        min_obstacles[0][0] = 0
        deque_cells = deque([(0, 0, 0)])
        while deque_cells:
            obstacles, row, col = deque_cells.popleft()
            for dr, dc in self._directions:
                new_row, new_col = row + dr, col + dc
                if _is_valid(new_row, new_col) and min_obstacles[new_row][
                    new_col
                ] == float("inf"):
                    if grid[new_row][new_col] == 1:
                        min_obstacles[new_row][new_col] = obstacles + 1
                        deque_cells.append((obstacles + 1, new_row, new_col))
                    else:
                        min_obstacles[new_row][new_col] = obstacles
                        deque_cells.appendleft((obstacles, new_row, new_col))
        return min_obstacles[m - 1][n - 1]


# Best / Most Optimal Solution
class Solution2:
    DIFFS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        grid = grid
        n_rows = len(grid)
        n_cols = len(grid[0])
        available = [[True] * n_cols for row in grid]
        available[0][0] = False
        in_progress = deque([(0, 0, 0)])
        while True:
            i, j, distance = in_progress.popleft()
            for di, dj in DIFFS:
                new_i = i + di
                new_j = j + dj
                if (
                    0 <= new_i < n_rows
                    and 0 <= new_j < n_cols
                    and available[new_i][new_j]
                ):
                    available[new_i][new_j] = False
                    if new_i == n_rows - 1 and new_j == n_cols - 1:
                        return distance
                    if grid[new_i][new_j] == 0:
                        in_progress.appendleft((new_i, new_j, distance))
                    else:
                        in_progress.append((new_i, new_j, distance + 1))
