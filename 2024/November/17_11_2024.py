from typing import List
from collections import deque


# My Solution
class Solution:
    def shortestSubarray(self, nums: List[int], target_sum: int) -> int:
        n = len(nums)
        prefix_sums = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]
        candidate_indices = deque()
        shortest_subarray_length = float("inf")
        for i in range(n + 1):
            while (
                candidate_indices
                and prefix_sums[i] - prefix_sums[candidate_indices[0]] >= target_sum
            ):
                shortest_subarray_length = min(
                    shortest_subarray_length, i - candidate_indices.popleft()
                )
            while (
                candidate_indices
                and prefix_sums[i] <= prefix_sums[candidate_indices[-1]]
            ):
                candidate_indices.pop()
            candidate_indices.append(i)
        return (
            shortest_subarray_length if shortest_subarray_length != float("inf") else -1
        )


# Best / Most Optimal Solution
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        shortest = float("inf")
        queue = deque([])
        total = currLen = 0
        for i, n in enumerate(nums):
            if n < 0:
                if total + n <= 0:
                    queue = deque([])
                    total = currLen = 0
                    continue
                else:
                    removed, removeLen = queue.pop()
                    curr = n + removed
                    stackLength = 1 + removeLen
                    while queue and curr < 0:
                        removed, removeLen = queue.pop()
                        curr += removed
                        stackLength += removeLen
                    total += n
                    queue.append((curr, stackLength))
                    currLen += 1
            else:
                queue.append((n, 1))
                total += n
                currLen += 1
            while queue and total >= k:
                shortest = min(shortest, currLen)
                removed, removeLen = queue.popleft()
                total -= removed
                currLen -= removeLen
        return shortest if shortest <= len(nums) else -1
