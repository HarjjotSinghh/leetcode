from typing import List
from bisect import bisect_right


# My Solution
class Solution:
    def maxTwoEvents(self, events):
        times = []
        for e in events:
            times.append([e[0], 1, e[2]])
            times.append([e[1] + 1, 0, e[2]])
        ans, max_value = 0, 0
        times.sort()
        for time_value in times:
            if time_value[1]:
                ans = max(ans, time_value[2] + max_value)
            else:
                max_value = max(max_value, time_value[2])
        return ans

# Best / Most Optimal Solution
class Solution2:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        max_weights = [0]
        max_weight_ends = [-1]
        events.sort(key = lambda x: x[1])
        max_two = 0
        for start, end, weight in events:
            index = bisect_right(max_weight_ends, start - 1) - 1
            if weight + max_weights[index] > max_two:
                max_two = weight + max_weights[index]
            if weight > max_weights[-1]:
                max_weights.append(weight)
                max_weight_ends.append(end)
        return max_two
