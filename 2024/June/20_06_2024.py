from typing import List

# My Solution
class Solution:
    def can_place_balls(self, x, position, m):
        prev_ball_pos = position[0]
        balls_placed = 1
        for i in range(1, len(position)):
            curr_pos = position[i]
            if curr_pos - prev_ball_pos >= x:
                balls_placed += 1
                prev_ball_pos = curr_pos
            if balls_placed == m:
                return True
        return False
    def maxDistance(self, position: List[int], m: int) -> int:
        answer = 0
        n = len(position)
        position.sort()
        low = 1
        high = int(position[-1] / (m - 1.0)) + 1
        while low <= high:
            mid = low + (high - low) // 2
            if self.can_place_balls(mid, position, m):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        return answer

# Best / Most Optimal Solution
class Solution2:
    def maxDistance(self, position: List[int], m: int) -> int:
        def check(minmax):
            rem = m - 1
            lim = position[0] + minmax
            for p in position[1:]:
                if p >= lim:
                    rem -= 1
                    lim = p + minmax
            return rem <= 0
        position.sort()
        if m == 2:
            return position[-1] - position[0]
        low = 1
        high = (position[-1] - position[0]) // (m - 1)
        while low < high:
            mid = (low + high + 1) // 2
            if check(mid):
                low = mid
            else:
                high = mid -1
        return low