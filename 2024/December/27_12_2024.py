from typing import List


# My Solution
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        max_left_score = values[0]
        max_score = 0
        for i in range(1, n):
            current_right_score = values[i] - i
            max_score = max(max_score, max_left_score + current_right_score)
            current_left_score = values[i] + i
            max_left_score = max(max_left_score, current_left_score)
        return max_score


# Best / Most Optimal Solution
class Solution2:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best_score = 0
        best_half_score = 0
        for value in values:
            best_half_score -= 1
            if best_half_score + value > best_score:
                best_score = best_half_score + value
            if value > best_half_score:
                best_half_score = value
        return best_score
