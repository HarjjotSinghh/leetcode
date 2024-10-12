from typing import List
import heapq

# My Solution
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        range_start = float("inf")
        range_end = float("-inf")
        for interval in intervals:
            range_start = min(range_start, interval[0])
            range_end = max(range_end, interval[1])
        point_to_count = [0] * (range_end + 2)
        for interval in intervals:
            point_to_count[
                interval[0]
            ] += 1
            point_to_count[
                interval[1] + 1
            ] -= 1
        concurrent_intervals = 0
        max_concurrent_intervals = 0
        for i in range(range_start, range_end + 1):
            concurrent_intervals += point_to_count[i]
            max_concurrent_intervals = max(
                max_concurrent_intervals, concurrent_intervals
            )
        return max_concurrent_intervals

# Best / Most Optimal Solution
class Solution2:
    def minGroups(self, intervals: List[List[int]]) -> int:
        min_heap = []
        intervals_sorted = sorted(intervals, key=lambda x:x[0])
        for start, end in intervals_sorted:
            if min_heap and min_heap[0] < start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, end)
        return len(min_heap)

