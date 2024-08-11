from typing import List

# My Solution
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def _count_islands():
            visited = set()
            count = 0
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        _explore_island(i, j, visited)
                        count += 1
            return count
        def _explore_island(i, j, visited):
            if (
                i < 0
                or i >= rows
                or j < 0
                or j >= cols
                or grid[i][j] == 0
                or (i, j) in visited
            ):
                return
            visited.add((i, j))
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                _explore_island(i + di, j + dj, visited)
        if _count_islands() != 1:
            return 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if _count_islands() != 1:
                        return 1
                    grid[i][j] = 1
        return 2
    
# Best / Most Optimal Solution
class Solution:
    DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    class ArticulationPointInfo:
        def __init__(self, has_articulation_point, time):
            self.has_articulation_point = has_articulation_point
            self.time = time
    def minDays(self, grid):
        rows, cols = len(grid), len(grid[0])
        ap_info = self.ArticulationPointInfo(False, 0)
        land_cells = 0
        island_count = 0
        discovery_time = [
            [-1] * cols for _ in range(rows)
        ]
        lowest_reachable = [
            [-1] * cols for _ in range(rows)
        ]
        parent_cell = [
            [-1] * cols for _ in range(rows)
        ]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    land_cells += 1
                    if discovery_time[i][j] == -1:
                        self._find_articulation_points(
                            grid,
                            i,
                            j,
                            discovery_time,
                            lowest_reachable,
                            parent_cell,
                            ap_info,
                        )
                        island_count += 1
        if island_count == 0 or island_count >= 2:
            return 0
        if land_cells == 1:
            return 1
        if ap_info.has_articulation_point:
            return 1
        return 2

    def _find_articulation_points(
        self,
        grid,
        row,
        col,
        discovery_time,
        lowest_reachable,
        parent_cell,
        ap_info,
    ):
        rows, cols = len(grid), len(grid[0])
        discovery_time[row][col] = ap_info.time
        ap_info.time += 1
        lowest_reachable[row][col] = discovery_time[row][col]
        children = 0
        for direction in self.DIRECTIONS:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if self._is_valid_land_cell(grid, new_row, new_col):
                if discovery_time[new_row][new_col] == -1:
                    children += 1
                    parent_cell[new_row][new_col] = (
                        row * cols + col
                    )
                    self._find_articulation_points(
                        grid,
                        new_row,
                        new_col,
                        discovery_time,
                        lowest_reachable,
                        parent_cell,
                        ap_info,
                    )
                    lowest_reachable[row][col] = min(
                        lowest_reachable[row][col],
                        lowest_reachable[new_row][new_col],
                    )
                    if (
                        lowest_reachable[new_row][new_col]
                        >= discovery_time[row][col]
                        and parent_cell[row][col] != -1
                    ):
                        ap_info.has_articulation_point = True
                elif new_row * cols + new_col != parent_cell[row][col]:
                    lowest_reachable[row][col] = min(
                        lowest_reachable[row][col],
                        discovery_time[new_row][new_col],
                    )
        if parent_cell[row][col] == -1 and children > 1:
            ap_info.has_articulation_point = True
    def _is_valid_land_cell(self, grid, row, col):
        rows, cols = len(grid), len(grid[0])
        return 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1
