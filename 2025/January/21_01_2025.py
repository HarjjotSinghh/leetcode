from typing import List


# My Solution
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        first_row_sum = sum(grid[0])
        second_row_sum = 0
        minimum_sum = float("inf")
        for turn_index in range(len(grid[0])):
            first_row_sum -= grid[0][turn_index]
            minimum_sum = min(minimum_sum, max(first_row_sum, second_row_sum))
            second_row_sum += grid[1][turn_index]
        return minimum_sum


# Best / Most Optimal Solution
class Solution2:
    def gridGame(self, grid: List[List[int]]) -> int:
        top_sum = sum(grid[0][1:])
        bottom_sum = 0
        optimal_result = max(top_sum, bottom_sum)
        for i in range(len(grid[0]) - 1):
            top_sum -= grid[0][i + 1]
            bottom_sum += grid[1][i]
            result = max(top_sum, bottom_sum)
            if result <= optimal_result:
                optimal_result = result
            else:
                break
        return optimal_result
