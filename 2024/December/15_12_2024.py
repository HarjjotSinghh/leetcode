from typing import List
from heapq import heapify, heappop, heappush
import math

# My Solution
class Solution:
    def maxAverageRatio(
        self, classes: List[List[int]], extraStudents: int
    ) -> float:
        def _calculate_gain(passes, total_students):
            return (passes + 1) / (total_students + 1) - passes / total_students
        max_heap = []
        for passes, total_students in classes:
            gain = _calculate_gain(passes, total_students)
            heappush(max_heap, (-gain, passes, total_students))
        for _ in range(extraStudents):
            current_gain, passes, total_students = heappop(max_heap)
            heappush(
                max_heap,
                (
                    -_calculate_gain(passes + 1, total_students + 1),
                    passes + 1,
                    total_students + 1,
                ),
            )
        total_pass_ratio = 0
        while max_heap:
            _, passes, total_students = heappop(max_heap)
            total_pass_ratio += passes / total_students
        return total_pass_ratio / len(classes)

# Best / Most Optimal Solution
class Solution2:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        classes = [(num/denom - (num+1)/(denom+1), num, denom) for num, denom in classes]
        heapify(classes)
        if classes[0][0]==0:
            return 1
        for i in range(extraStudents):
            _, num, denom = heappop(classes)
            heappush(classes, ((num+1)/(denom+1) - (num+2)/(denom+2), num+1, denom+1))
        return sum([c[1]/c[2] for c in classes])/len(classes)
