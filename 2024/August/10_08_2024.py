from typing import List

# My Solution
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        grid_size = len(grid)
        points_per_side = grid_size + 1
        total_points = points_per_side * points_per_side
        parent_array = [-1] * total_points
        for i in range(points_per_side):
            for j in range(points_per_side):
                if (
                    i == 0
                    or j == 0
                    or i == points_per_side - 1
                    or j == points_per_side - 1
                ):
                    point = i * points_per_side + j
                    parent_array[point] = 0
        parent_array[0] = -1
        region_count = 1
        for i in range(grid_size):
            for j in range(grid_size):
                if grid[i][j] == "/":
                    top_right = i * points_per_side + (j + 1)
                    bottom_left = (i + 1) * points_per_side + j
                    region_count += self._union(
                        parent_array, top_right, bottom_left
                    )
                elif grid[i][j] == "\\":
                    top_left = i * points_per_side + j
                    bottom_right = (i + 1) * points_per_side + (j + 1)
                    region_count += self._union(
                        parent_array, top_left, bottom_right
                    )
        return region_count
    def _find(self, parent_array: List[int], node: int) -> int:
        if parent_array[node] == -1:
            return node
        parent_array[node] = self._find(parent_array, parent_array[node])
        return parent_array[node]
    def _union(self, parent_array: List[int], node1: int, node2: int) -> int:
        parent1 = self._find(parent_array, node1)
        parent2 = self._find(parent_array, node2)
        if parent1 == parent2:
            return 1
        parent_array[parent2] = parent1
        return 0

# Best / Most Optimal Solution
class Solution2:
    def regionsBySlashes(self, grid: List[str]) -> int:
        dots = len(grid) + 1
        parent = [i for i in range(dots*dots)]
        count = 1
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            if parent_x != parent_y:
                if parent_x < parent_y:
                    parent[parent_y] = parent_x
                else:
                    parent[parent_x] = parent_y
                return False
            return True
        for i in range(dots):
            for j in range(dots):
                if i == 0 or j == 0 or i == dots-1 or j == dots-1:
                    cell = i * dots + j
                    union(dots, cell)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == ' ':
                    continue
                if grid[i][j] == '/':
                    cell1 = (i+1) * dots + j
                    cell2 = i * dots + j + 1
                    if union(cell1, cell2):
                        count += 1
                elif grid[i][j] == "\\":
                    cell1 = i * dots + j
                    cell2 = (i+1) * dots + j + 1
                    if union(cell1, cell2):
                        count += 1
        return count