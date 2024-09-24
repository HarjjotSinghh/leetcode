from typing import List

# My Solution
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        cols = len(points[0])
        current_row = [0] * cols
        previous_row = [0] * cols
        for row in points:
            running_max = 0
            for col in range(cols):
                running_max = max(running_max - 1, previous_row[col])
                current_row[col] = running_max
            running_max = 0
            for col in range(cols - 1, -1, -1):
                running_max = max(running_max - 1, previous_row[col])
                current_row[col] = max(current_row[col], running_max) + row[col]
            previous_row = current_row.copy()
        return max(previous_row)

# Best / Most Optimal Solution
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        dp = [0] * n
        for i in range(m):
            newDp = [0] * n
            for j in range(n):
                point = points[i][j]
                if i > 0:
                    point += dp[j]
                if j > 0:
                    if point > newDp[j - 1] - 1:
                        k = j
                        while k >= 0 and newDp[k] < point:
                            newDp[k] = point
                            k -= 1
                            point -= 1
                    else:
                        newDp[j] = newDp[j - 1] - 1
                else:
                    newDp[j] = point
            dp = newDp
        return max(dp)
